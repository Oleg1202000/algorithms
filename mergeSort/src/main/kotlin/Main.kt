package org.example

fun main() {
    val nums: IntArray = intArrayOf(2, 2, 1, 3, 1, 10, 1, 2, 2, -10, 0, -100)

    val arrSorted = merge(nums)

    arrSorted.map {
        print("$it ")
    }
}


private fun merge(nums: IntArray): IntArray {
    if (nums.size != 1) {
        val arrLeft = merge(nums.slice(0..<nums.size/2).toIntArray())
        val arrRight = merge(nums.slice(nums.size/2..<nums.size).toIntArray())

        return sort(arrLeft, arrRight)
    } else {
        return nums
    }
}


private fun sort(leftArr: IntArray, rightArr: IntArray): IntArray {
    val listSorted: MutableList<Int> = mutableListOf()
    var leftIndex = 0
    var rightIndex = 0

    while (leftIndex < leftArr.size && rightIndex < rightArr.size) {

        if (leftArr[leftIndex] <= rightArr[rightIndex]) {
            listSorted.add(leftArr[leftIndex])
            leftIndex++
        } else if (leftArr[leftIndex] > rightArr[rightIndex]) {
            listSorted.add(rightArr[rightIndex])
            rightIndex++
        }
    }

    while (leftIndex == leftArr.size && rightIndex < rightArr.size) {
        listSorted.add(rightArr[rightIndex])
        rightIndex++
    }

    while (rightIndex == rightArr.size && leftIndex < leftArr.size) {
        listSorted.add(leftArr[leftIndex])
        leftIndex++
    }

    return listSorted.toIntArray()
}
