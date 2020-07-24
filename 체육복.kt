
    fun solution(n: Int, lost: IntArray, reserve: IntArray): Int {
        var answer = n
        var myArray = IntArray(n+2, {1})
        print(myArray[0])
        myArray[0]=0
        myArray[n-1]=0

        for (lostp in lost){
            myArray[lostp] -=1
        }
        for (reservep in reserve){
            myArray[reservep] +=1
        }
        


        return answer
    }
    

fun main(){
    val array= intArrayOf(1,2)
    val array2 = intArrayOf(3)
    val mysolution= Solution()
    
    Solution().solution(5, array,array2)
}