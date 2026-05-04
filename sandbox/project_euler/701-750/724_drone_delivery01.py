import random
import matplotlib.pyplot as plt

def draw_state(ax, distances, speeds, selected, trial, trials, step,
               running_ev, just_finished=False):
    """
    Draw the current state of the drones.
    """
    n = len(distances)
    yvals = list(range(n, 0, -1))   # top to bottom lanes: n, n-1, ..., 1

    ax.clear()

    xmax = max(10, max(distances) + 3)

    # road / lanes
    for y in yvals:
        ax.hlines(y, 0, xmax, color="lightgray", linewidth=1)

    # depot
    ax.axvline(0, color="black", linewidth=2)
    ax.text(0, n + 0.35, "Depot", ha="left", va="bottom", fontsize=10)

    # colors
    colors = []
    for i in range(n):
        if just_finished:
            colors.append("tab:green")
        elif i == selected:
            colors.append("tab:red")
        else:
            colors.append("tab:blue")

    # drones
    ax.scatter(distances, yvals, s=250, c=colors, zorder=3)

    # labels
    for i, (x, y, v) in enumerate(zip(distances, yvals, speeds), start=1):
        ax.text(x, y, f"D{i}", ha="center", va="center",
                color="white", weight="bold", fontsize=9)
        ax.text(x, y + 0.28, f"v={v}", ha="center", va="bottom", fontsize=9)

    # title
    if just_finished:
        trial_avg = sum(distances) / n
        title = (f"Trial {trial}/{trials}   Step {step}   "
                 f"Running E(5) ≈ {running_ev:.5f}   "
                 f"Trial average = {trial_avg:.5f}")
    else:
        title = (f"Trial {trial}/{trials}   Step {step}   "
                 f"Running E(5) ≈ {running_ev:.5f}")

    ax.set_title(title)

    # small status note
    if just_finished:
        msg = "Packages dropped"
    else:
        msg = f"Selected drone: D{selected + 1}"
    ax.text(0.99, 0.02, msg, transform=ax.transAxes,
            ha="right", va="bottom", fontsize=10)

    ax.set_xlim(-1, xmax)
    ax.set_ylim(0.5, n + 0.8)
    ax.set_xlabel("Distance from depot (cm)")
    ax.set_yticks(yvals)
    ax.set_yticklabels([f"Drone {i}" for i in range(1, n + 1)])


def animate_drones(n=5, trials=1000, move_pause=0.2, trial_pause=1.0, seed=None):
    if seed is not None:
        random.seed(seed)

    running_total = 0.0

    plt.ion()
    fig, ax = plt.subplots(figsize=(11, 5))

    for trial in range(1, trials + 1):
        distances = [0] * n
        speeds = [0] * n
        has_not_moved = n
        step = 0

        while has_not_moved > 0:
            k = random.randrange(n)

            # selected drone gets instruction
            if speeds[k] == 0:
                speeds[k] = 1
                has_not_moved -= 1
            else:
                speeds[k] += 1

            # one second passes; all moving drones advance
            distances = [d + s for d, s in zip(distances, speeds)]
            step += 1

            # running estimate only changes after completed trials
            running_ev = running_total / (trial - 1) if trial > 1 else 0.0

            draw_state(ax, distances, speeds, k, trial, trials, step,
                       running_ev, just_finished=False)
            plt.pause(move_pause)

        # end of trial
        trial_avg = sum(distances) / n
        running_total += trial_avg
        running_ev = running_total / trial

        draw_state(ax, distances, speeds, None, trial, trials, step,
                   running_ev, just_finished=True)
        plt.pause(trial_pause)

    plt.ioff()
    print(f"For n = {n}, Expected Value ≈ {running_total / trials:.5f}")
    plt.show()


# run it
animate_drones(n=5, trials=100, move_pause=0.05, trial_pause=1., seed=1)
