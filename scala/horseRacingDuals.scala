import math._
import scala.util._
import scala.io.StdIn._
import scala.collection.mutable 

object Solution extends App {
    val n = readLine.toInt
    var strength = mutable.TreeSet[Int]()

    for(i <- 0 until n) {
        strength += readLine.toInt
    }

    Console.err.println(s"Debug messages $strength")

    var min = Integer.MAX_VALUE

    val it = strength.iterator
    var prev = it.next()
    while (it.hasNext) {
        var curr = it.next();
        if (curr-prev < min)
            min = curr-prev;
        prev = curr;
    }

    println(min)
}