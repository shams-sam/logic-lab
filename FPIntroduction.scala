// https://www.hackerrank.com/challenges/fp-hello-world-n-times
def f(n: Int) = List.fill(n)(1).map(i => println("Hello World"))
def f(n: Int) = (1 to n) foreach(i => println("Hello World"))
// https://www.hackerrank.com/challenges/fp-list-replication
def f(num:Int,arr:List[Int]):List[Int] = arr.map(List.fill(num)(_)).reduce(_ ++ _)
def f(num:Int,arr:List[Int]):List[Int] = arr.flatMap(List.fill(num)(_))
// https://www.hackerrank.com/challenges/fp-filter-array
def f(delim:Int,arr:List[Int]):List[Int] = arr.filter(_ < delim)
// https://www.hackerrank.com/challenges/fp-filter-positions-in-a-list
def f(arr:List[Int]):List[Int] = arr.zipWithIndex.filter(_._2 % 2 != 0).map(_._1)

List.fill(io.Source.stdin.getLines().take(1).toList(0).toInt)(io.Source.stdin.getLines().take(1).toList(0))

