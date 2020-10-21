import math._
import scala.util._
import scala.io.StdIn._

object Solution extends App {
    def getClosest(numbers: Array[Int]) = {
        val positivesNumbers : Array[Int] =  numbers.filter(_ >= 0)
        val negativesNumbers : Array[Int] =  numbers.filter(_ <= 0)
        
        val minPositive :Int = Try(positivesNumbers.min).toOption match {
            case None => 5526
            case Some(value) => value
        }

        val maxNegative :Int = Try(negativesNumbers.max).toOption match {
            case None => -273
            case Some(value) => value
        }

        if (minPositive == maxNegative.abs) {
            println(minPositive)
        } else if ((minPositive min maxNegative.abs) == minPositive) {
            println(minPositive)
        } else {
            println(maxNegative)
        }
    }

    val n = readLine.toInt // the number of temperatures to analyse
    var inputs = (readLine split " ")

    n match {
        case 0 => println(0)
        case 1 => println(inputs(0))
        case _ => getClosest(inputs.map(_.toInt))
    }
}
