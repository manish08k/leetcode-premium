/**
 * @param {string} start
 * @param {string} end
 * @param {number} step
 * @yields {string}
 */
var dateRangeGenerator = function* (start, end, step) {
  const curr = new Date(start);
  const endTime = new Date(end).getTime();

  while (curr.getTime() <= endTime) {
    const date = String(curr.getDate()).padStart(2, '0');
    const month = String(curr.getMonth() + 1).padStart(2, '0');
    const year = String(curr.getFullYear()).padStart(2, '0');
    yield `${year}-${month}-${date}`;

    const next = curr.getDate() + step;
    curr.setDate(next);
  }
};

/**
 * const g = dateRangeGenerator('2023-04-01', '2023-04-04', 1);
 * g.next().value; // '2023-04-01'
 * g.next().value; // '2023-04-02'
 * g.next().value; // '2023-04-03'
 * g.next().value; // '2023-04-04'
 * g.next().done; // true
 */