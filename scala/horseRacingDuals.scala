import math._
import scala.util._
import scala.io.StdIn._

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
object Solution extends App {
    val n = readLine.toInt
    for(i <- 0 until n) {
        val pi = readLine.toInt
        println(pi)
    }
    
    // Write an answer using println
    // To debug: Console.err.println("Debug messages...")
    
    println("answer")
}

object Solution extends App {
    val n = readLine.toInt
    var strength = new mutable.ListBuffer[Int]()

    for(i <- 0 until n) {
        strength += readLine.toInt
    }

    var s = strength.toList.sorted

    Console.err.println(s"Debug messages $s")

    var strengthDiff = new mutable.ListBuffer[Int]()

    for(i <- 0 until n - 1) {
        strengthDiff += (s(i) - s(i+1)).abs 
    }

    assert(strength.size > strengthDiff.size)

    println(strengthDiff.toList.min)
}
