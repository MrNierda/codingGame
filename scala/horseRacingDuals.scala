import math._
import scala.util._
import scala.io.StdIn._
import scala.collection.mutable 

object Solution extends App {
    val n = readLine.toInt
    var strength = mutable.ListBuffer[Int]()

    var minStrengthDiff = Integer.MAX_VALUE

    for(i <- 0 until n) {
        strength += readLine.toInt
    }

    if (strength.toSet.size == 1) {
        minStrengthDiff = 0
    }

    strength = strength.sorted

    val it = strength.iterator
    var previousHorse = it.next()
    while (it.hasNext) {
        var currentHorse = it.next();
        if (currentHorse - previousHorse < minStrengthDiff)
            minStrengthDiff = currentHorse - previousHorse;
        previousHorse = currentHorse;
    }

    println(minStrengthDiff)
}