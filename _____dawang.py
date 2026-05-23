"""
Interview Problem: Busiest 2-Hour Window
====================================================
Given a list of 4-digit timestamps in HHMM format (e.g. 0900, 1158, 2300),
find the 2-hour sliding window that contains the most timestamps.

The window does not need to align to a fixed grid — it can start at any
minute (e.g. 11:58 to 13:58 is valid).

Input : list of ints in HHMM format
Output: (start_hhmm, end_hhmm, count)
"""

# Note: they may have also asked the question where like if it is a 2 hour window, (900-1100) 
#  1100 may not be included in the window. I don't remember exactly though
# I would recommend doing the other find top k elements as well just in case this isnt the question.
# I did it using the first method with a helper function and sliding window approach and I passed all test cases.
# also remember time and space complexity of the solution.
# I also used default dict to store the count of the timestamps.
# which may be easier.


import heapq


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def to_minutes(ts: int) -> int:
    """Convert a 4-digit HHMM timestamp to total minutes since midnight."""
    return (ts // 100) * 60 + (ts % 100)


def to_hhmm(minutes: int) -> int:
    """Convert total minutes since midnight back to HHMM format."""
    return (minutes // 60) * 100 + (minutes % 60)


# ---------------------------------------------------------------------------
# Approach 1: Sliding Window  —  O(n log n) time, O(n) space
# ---------------------------------------------------------------------------

def busiest_window(timestamps: list[int]) -> tuple[int, int, int]:
    """
    Return the 2-hour window (start, end, count) with the most timestamps.

    Strategy:
      1. Convert every timestamp to minutes and sort.
      2. Use two pointers (left, right). For each right pointer position,
         shrink left until the window fits within 120 minutes.
      3. Track the widest window seen (most timestamps inside).
    """
    if not timestamps:
        return (0, 0, 0)

    mins = sorted(to_minutes(ts) for ts in timestamps)
    n = len(mins)

    best_count = 0
    best_left = 0
    left = 0

    for right in range(n):
        # Shrink from the left while the window exceeds 120 minutes
        while mins[right] - mins[left] > 120:
            left += 1

        window_count = right - left + 1
        if window_count > best_count:
            best_count = window_count
            best_left = left

    start = to_hhmm(mins[best_left])
    end = to_hhmm(mins[best_left + best_count - 1])
    return (start, end, best_count)


# ---------------------------------------------------------------------------
# Approach 2: Heap — top K busiest windows  —  O(n log K) heap phase
# ---------------------------------------------------------------------------

def top_k_windows(timestamps: list[int], k: int) -> list[tuple[int, int, int]]:
    """
    Return the top K non-overlapping 2-hour windows ranked by timestamp count.

    Strategy:
      1. Same sliding window pass as above, but record every candidate window
         as (count, start_minutes, end_minutes).
      2. Maintain a min-heap of size K so we always keep the K largest counts.
         Pushing/popping from a min-heap of size K is O(log K) per operation.
      3. Return results sorted descending by count.

    Note: "candidate window" here means the window anchored at each right
    pointer position — the densest window that ends at that timestamp.
    """
    if not timestamps:
        return []

    mins = sorted(to_minutes(ts) for ts in timestamps)
    n = len(mins)

    # min-heap stores (count, start_min, end_min)
    heap: list[tuple[int, int, int]] = []
    left = 0

    for right in range(n):
        while mins[right] - mins[left] > 120:
            left += 1

        count = right - left + 1
        start_min = mins[left]
        end_min = mins[right]

        if len(heap) < k:
            heapq.heappush(heap, (count, start_min, end_min))
        elif count > heap[0][0]:
            heapq.heapreplace(heap, (count, start_min, end_min))

    # Convert back to HHMM and sort descending by count
    results = [
        (to_hhmm(start), to_hhmm(end), count)
        for count, start, end in heap
    ]
    results.sort(key=lambda x: -x[2])
    return results


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    def fmt(result):
        start, end, count = result
        return f"{start:04d}–{end:04d} ({count} people)"

    # --- Test 1: basic clustering ---
    ts1 = [900, 930, 1000, 1030, 1100, 1130, 1200, 2300]
    # Each consecutive pair is 30 min apart; 5 fit in any 120-min window
    # e.g. 0900–1100 contains: 900, 930, 1000, 1030, 1100 = 5 timestamps
    result1 = busiest_window(ts1)
    print("Test 1:", fmt(result1))
    assert result1[2] == 5, f"Expected 5, got {result1[2]}"

    # --- Test 2: all timestamps within 2 hours ---
    ts2 = [1158, 1200, 1215, 1300, 1330, 1355]
    result2 = busiest_window(ts2)
    print("Test 2:", fmt(result2))
    assert result2[2] == 6, f"Expected 6, got {result2[2]}"

    # --- Test 3: single timestamp ---
    ts3 = [1200]
    result3 = busiest_window(ts3)
    print("Test 3:", fmt(result3))
    assert result3[2] == 1

    # --- Test 4: timestamps spread far apart ---
    ts4 = [100, 500, 900, 1400, 1900, 2300]
    result4 = busiest_window(ts4)
    print("Test 4:", fmt(result4))
    assert result4[2] == 1  # no two are within 2 hours

    # --- Test 5: top_k_windows ---
    ts5 = [900, 930, 1000, 1030, 1100, 1130, 1200, 1500, 1530, 1600, 2300]
    top3 = top_k_windows(ts5, k=3)
    print("Test 5 top-3:")
    for w in top3:
        print(" ", fmt(w))
    assert top3[0][2] >= top3[1][2] >= top3[2][2]

    print("\nAll tests passed.")
