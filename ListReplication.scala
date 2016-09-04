object ListReplication {
    def f(x: Int, s: List[Int]): List[Int] = {
        s.map(_ * x)
    }

    def main(args: Array[String]): Unit = {
        val x = io.Source.stdin.readInt
        println(x)
    }
}