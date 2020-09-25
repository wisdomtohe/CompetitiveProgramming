package leetcode.easy;
//https://leetcode.com/problems/max-consecutive-ones/
public class MaxConsequetiveOnes {

    public int findMaxConsecutiveOnes(int[] nums) {
	int counter = 0;
	int maxCounter = 0;
	for (int i = 0; i < nums.length; i++) {
	    if (nums[i] == 1) {
		while (i < nums.length && nums[i] != 0) {
		    counter++;
		    i++;
		}
	    }
	    if (counter > maxCounter) {
		maxCounter = counter;
	    }
	    counter = 0;
	}
	return maxCounter;
    }

}
