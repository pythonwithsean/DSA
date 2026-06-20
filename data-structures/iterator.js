/* ----------------------------------------------------------------------------
 * 1. The manual iterator (what you already understand)
 *
 *    An iterator is just an object with a next() method that returns
 *    { value, done }. `curr` is the "where we are" state you mentioned.
 * ------------------------------------------------------------------------- */
function makeRangeIterator(start, end) {
  let curr = start; // <-- the position state lives in this closure variable

  return {
    next() {
      if (curr < end) {
        return { value: curr++, done: false };
      }
      return { value: undefined, done: true };
    },
  };
}

function demoManualIterator() {
  banner('1. Manual iterator');
  const it = makeRangeIterator(0, 3);
  console.log(it.next()); // { value: 0, done: false }
  console.log(it.next()); // { value: 1, done: false }
  console.log(it.next()); // { value: 2, done: false }
  console.log(it.next()); // { value: undefined, done: true }
  console.log(it.next()); // still done — an exhausted iterator stays exhausted
}


/* ----------------------------------------------------------------------------
 * 2. Making something ITERABLE (so for...of works)
 *
 *    An object becomes iterable by having a [Symbol.iterator]() method that
 *    returns a fresh iterator. This is the iterable-vs-iterator split:
 *    the Range object is the factory; each for...of asks it for a new cursor.
 * ------------------------------------------------------------------------- */
class Range {
  constructor(start, end) {
    this.start = start;
    this.end = end;
  }

  // Called by for...of, spread (...), Array.from, destructuring, etc.
  // Returns a NEW iterator every time => the iterable can be reused.
  [Symbol.iterator]() {
    return makeRangeIterator(this.start, this.end);
  }
}

function demoIterable() {
  banner('2. Iterable vs iterator');
  const r = new Range(0, 3);

  // Reusable: each loop gets its own fresh cursor starting from the beginning.
  console.log('first  loop:', [...r]); // [ 0, 1, 2 ]
  console.log('second loop:', [...r]); // [ 0, 1, 2 ]  <- works again

  // The raw iterator, by contrast, is single-use:
  const it = r[Symbol.iterator]();
  console.log('drain once: ', [...{ [Symbol.iterator]: () => it }]); // [0,1,2]
  console.log('drain again:', [...{ [Symbol.iterator]: () => it }]); // []  exhausted
}


/* ----------------------------------------------------------------------------
 * 3. The generator version of the SAME range
 *
 *    `function*` makes a generator function. `yield` hands out a value and
 *    freezes the function. You never wrote next() or done — the engine builds
 *    them. The local `curr` survives across pauses automatically.
 *
 *    Bonus: a generator object is BOTH an iterator and an iterable, so you can
 *    drop it straight into for...of.
 * ------------------------------------------------------------------------- */
function* range(start, end) {
  for (let curr = start; curr < end; curr++) {
    yield curr; // pause here, hand out curr, resume on the next .next()
  }
}

function demoGenerator() {

  // Step it by hand to see the iterator protocol underneath:
  const g = range(0, 3);
  console.log(g.next()); // { value: 0, done: false }
  console.log(g.next()); // { value: 1, done: false }
  console.log(g.next()); // { value: 2, done: false }
  console.log(g.next()); // { value: undefined, done: true }

  // Or just consume it like any iterable:
  const collected = [];
  for (const n of range(0, 3)) collected.push(n);
  console.log('for...of:', collected); // [ 0, 1, 2 ]
}


/* ----------------------------------------------------------------------------
 * 4. Proof that a generator is LAZY (pause/resume, runs nothing until asked)
 *
 *    Calling a generator function runs ZERO lines of its body. The body only
 *    advances when you pull a value with .next() (or for...of).
 * ------------------------------------------------------------------------- */
function* noisy() {
  console.log('   [generator body actually started running now]');
  yield 1;
  console.log('   [resumed after the first yield]');
  yield 2;
}

function demoLaziness() {
  banner('4. Generators are lazy');
  const g = noisy();
  console.log('called noisy() — notice nothing from the body has printed yet');
  console.log('pulling first value...');
  console.log(g.next()); // NOW the body starts, prints, then yields 1
  console.log('pulling second value...');
  console.log(g.next()); // resumes right after the first yield
}


/* ----------------------------------------------------------------------------
 * 5. Infinite sequences — the payoff of laziness
 *
 *    You can't build an infinite array. You CAN build an infinite generator
 *    and take only what you need, computed on demand.
 * ------------------------------------------------------------------------- */
function* naturals() {
  let n = 0;
  while (true) yield n++; // never terminates — but that's fine, it's lazy
}

function take(count, iterable) {
  const out = [];
  for (const x of iterable) {
    if (out.length >= count) break; // stop pulling once we have enough
    out.push(x);
  }
  return out;
}

function demoInfinite() {
  banner('5. Infinite generator + lazy take()');
  console.log('first 5 naturals:', take(5, naturals())); // [0,1,2,3,4]
  console.log('first 3 naturals:', take(3, naturals())); // [0,1,2]
}


/* ----------------------------------------------------------------------------
 * 6. yield* — delegating to another generator (clean recursion)
 *
 *    `yield* otherGenerator` yields everything that the other one yields.
 *    This makes recursive walks (trees, nested structures) read naturally.
 * ------------------------------------------------------------------------- */
const tree = {
  value: 1,
  children: [
    { value: 2, children: [{ value: 4 }, { value: 5 }] },
    { value: 3, children: [{ value: 6 }] },
  ],
};

function* walk(node) {
  yield node.value;
  for (const child of node.children ?? []) {
    yield* walk(child); // delegate: re-yield everything the child walk produces
  }
}

function demoDelegation() {
  banner('6. yield* delegation (depth-first tree walk)');
  console.log('tree values:', [...walk(tree)]); // [ 1, 2, 4, 5, 3, 6 ]
}


/* ----------------------------------------------------------------------------
 * 7. A generator's return value
 *
 *    `return x` inside a generator ends it and puts x on the FINAL result
 *    ({ value: x, done: true }). for...of ignores that final value; manual
 *    .next() can see it.
 * ------------------------------------------------------------------------- */
function* withReturn() {
  yield 'a';
  yield 'b';
  return 'THE RETURN VALUE';
}

function demoReturnValue() {
  banner('7. return value in a generator');
  const g = withReturn();
  console.log(g.next()); // { value: 'a', done: false }
  console.log(g.next()); // { value: 'b', done: false }
  console.log(g.next()); // { value: 'THE RETURN VALUE', done: true }

  // for...of only iterates the yielded values, never the returned one:
  console.log('for...of sees:', [...withReturn()]); // [ 'a', 'b' ]
}


/* ----------------------------------------------------------------------------
 * 8. Two-way communication — generators are coroutines (advanced)
 *
 *    `yield` is an expression. A value passed to .next(value) becomes the
 *    result of the yield that the generator is currently paused on. This lets
 *    data flow BACK INTO the generator, which is what makes it a coroutine.
 *
 *    Note the "priming" call: the first .next() just runs up to the first
 *    yield (its argument is discarded), because there's no paused yield yet.
 * ------------------------------------------------------------------------- */
function* runningTotal() {
  let total = 0;
  while (true) {
    const x = yield total; // hand out the current total, then wait for input
    total += x; // x is whatever the caller passes to .next(x)
  }
}

function demoCoroutine() {
  banner('8. Two-way: passing values INTO a generator');
  const acc = runningTotal();
  console.log(acc.next().value);   // 0   <- priming call, gets initial total
  console.log(acc.next(10).value); // 10  <- sends 10, total = 10
  console.log(acc.next(5).value);  // 15  <- sends 5,  total = 15
  console.log(acc.next(100).value);// 115
}


/* ============================================================================
 *  Run the whole tour
 * ========================================================================= */
demoManualIterator();
demoIterable();
demoGenerator();
demoLaziness();
demoInfinite();
demoDelegation();
demoReturnValue();
demoCoroutine();
