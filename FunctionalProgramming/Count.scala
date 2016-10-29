object Count {
    def main(args: Array[String]) {
        println(io.Source.stdin.getLines.takeWhile(_ != "").map(_ => 1).sum)
    }
}