from scipy.spatial.distance import cdist
from scipy.optimize import linear_sum_assignment as lsa
import numpy as np

# Linear Sum Assignment
def trace(new_positions, traces, frame):
    """
    1D LSA CODE
    """
    # new_positions=new_particles
    # traces=positions of particles of the previous frame
    # frame=current frame in video that is being examined

    # trace(new_particles, Particles, frame_i) as represented in the get particle trace code below

    if len(traces[0]) > 0:
        trace_pos = []
        for trace in traces[0]:
            last_pos = np.array(
                trace[-1][1:3]
            )  # find the list of all positions in the last frame

            if len(trace) > 2:
                last_pos += np.mean(
                    np.diff(np.array(trace)[:, 1:3], axis=0), axis=0
                )

            trace_pos.append(
                last_pos
            )  # Positions of last frame are stores in trace_pos

        distance_mat = cdist(
            np.array(new_positions)[:, 0:2], np.array(trace_pos)
        )
        distance_mat[distance_mat > 30] = 100000
        row, col = lsa(
            distance_mat
        )  # solve the linear sum assignment problem (how to assign old particle detections to new detections in such a way that the sum of the distance between old and new detections is minimized)

        isinf = np.nonzero(distance_mat[row, col] > 10000)

        row = np.delete(row, isinf)
        col = np.delete(
            col, isinf
        )  # remove assignments of particles that are too far away from each other

        for c, r in zip(col[:], row[:]):
            traces[0][c].append([frame, *np.array(new_positions[r])])

        new_positions = np.delete(new_positions, row, axis=0)

    for i in range(
        len(new_positions)
    ):  # len(new_positions) is number of particles in that particular frame
        traces[0].append(
            [[frame, *np.array(new_positions[i])]]
        )  # Notice that it is array of array
        # Now the Particles array is filled with the frame number-0 and the particle positions of first frame
    return traces


def get_particle_trace(
    Video,
):  # the limit for finding particle positions in get_positions

    # The following code shows how to call the trace function and build a trace
    _traces = [[]]
    _completed_traces = []
    for _frame in range(len(Video)):
        # new_particles=get_positions_video_frame(Video, frame_i, limit) #This is a function which takes a video and returns the positions of all particles in the Video at frame frame_i
        _new_positions = Video[
            _frame
        ]  # This is the difference between get_particle_trace and get_particle_trace_2
        trace(_new_positions, _traces, _frame)
        for particle_trace in _traces[0]:

            if (
                particle_trace[-1][0] != _frame and len(particle_trace) >= 10
            ):  # -1 is the last element in the array
                _completed_traces.append(
                    particle_trace
                )  # If no particle in the current frame was added to particle_trace, add this trace to completed_traces

        _traces[0] = [
            _pos for _pos in _traces[0] if _pos[-1][0] == _frame
        ]  # Keep only those traces which were updated
        # After completion, completed_traces contains all particles which were tracked and lost at some point during the video (since the detections are flickering, almost all relevant data will be stored here), Particles contain all traces which are currently being tracked

    return _traces, _completed_traces
