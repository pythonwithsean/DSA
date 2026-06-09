"""
Approach: Heap + Hash Map + Lazy Deletion

We need to support:

1. updatePriority(eventId, newPriority)
2. pollHighest()

A heap is great for finding the highest priority event in O(log n),
but updating an arbitrary element already inside a heap is expensive.

Instead of trying to find and modify the old heap entry, we use
"lazy deletion".

--------------------------------------------------------------------
Data Structures
--------------------------------------------------------------------

heap:
    Stores tuples (-priority, eventId)

    We negate the priority because Python's heapq is a min-heap.

    Example:

        priority = 10, eventId = 5

        stored as:

            (-10, 5)

    The heap compares tuples lexicographically:

        (-10, 2) < (-10, 5)

    so for equal priorities, the smaller eventId is automatically
    chosen first.

table:
    Hash map:

        eventId -> current priority

    This is the source of truth.

    The heap may contain stale entries due to updates, but the table
    always contains the current priority for every active event.

--------------------------------------------------------------------
Update
--------------------------------------------------------------------

Suppose:

    event 5 has priority 10

Heap:

    (-10, 5)

Now:

    updatePriority(5, 20)

Instead of removing (-10, 5) from the heap, we simply:

    table[5] = 20
    heappush((-20, 5))

Heap now contains:

    (-20, 5)   <- valid
    (-10, 5)   <- stale

The old entry is left inside the heap.

This is called lazy deletion.

--------------------------------------------------------------------
Poll
--------------------------------------------------------------------

Before using the heap top, we verify it is still valid.

An entry is stale if:

1. The event was already removed

       eventId not in table

2. The priority no longer matches the current priority

       heap_priority != table[eventId]

If either condition is true, we discard the heap entry and continue.

Eventually the heap top will be a valid active event.

When we poll an event:

    del table[eventId]

This marks the event as inactive.

Any future heap entries for that event become stale and will be
discarded when they reach the top.

--------------------------------------------------------------------
Complexity
--------------------------------------------------------------------

Initialization:
    O(n)

updatePriority:
    O(log n)

pollHighest:
    Amortized O(log n)

Although a poll may remove several stale entries, each stale entry
is removed at most once during the lifetime of the program.

Therefore total work remains:

    O((n + updates) log n)

which satisfies the constraints.

"""

import heapq

class EventManager:

    def __init__(self, events: list[list[int]]):
        self.heap = [(-p[1], p[0]) for p in events]
        heapq.heapify(self.heap)
        self.table = {}
        # we know all ids are unique
        for prio,id in self.heap:
            self.table[id] = -prio

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.table[eventId] = newPriority
        heapq.heappush(self.heap,(-newPriority,eventId))

    def pollHighest(self) -> int:
        # we want the smallest eventId if multiple with same prio
        # remove useless ones that might be on top
        while self.heap and (self.heap[0][1] in self.table and -self.heap[0][0] != self.table[self.heap[0][1]] or self.heap[0][1] not in self.table):
            heapq.heappop(self.heap)
        if self.heap:
            top_prio,top_id = heapq.heappop(self.heap)
            del self.table[top_id]
            return top_id
        return -1




# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()
