<h2><a href="https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/">1007. Minimum Domino Rotations For Equal Row</a></h2><h3>Medium</h3><hr><div><p>In a row of dominoes, <code>tops[i]</code> and <code>bottoms[i]</code> represent the top and bottom halves of the <code>i<sup>th</sup></code> domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)</p>

<p>We may rotate the <code>i<sup>th</sup></code> domino, so that <code>tops[i]</code> and <code>bottoms[i]</code> swap values.</p>

<p>Return the minimum number of rotations so that all the values in <code>tops</code> are the same, or all the values in <code>bottoms</code> are the same.</p>

<p>If it cannot be done, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/14/domino.png" style="height: 300px; width: 421px;">
<pre><strong>Input:</strong> tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
<strong>Output:</strong> -1
<strong>Explanation:</strong> 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= tops.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>bottoms.length == tops.length</code></li>
	<li><code>1 &lt;= tops[i], bottoms[i] &lt;= 6</code></li>
</ul>
</div>

# Notes

We have two arrays, the first one represents the values on the top and second array represents the bottom
The values that the dominoes can take are 1 through 6
We need to find the minimum number of rotations to be made so that all the values on one side (either top or bottom) are the same in value
If its not possible we return -1


For this to be successful, the two arrays must have an element common and this element shhould appear in all positions, either in the first array or the second
Then we determine the minimum number of rotaions that need to be made.

Since the cells in the arrays can only have values from 1 to 6 we check if 1 is appearing in any one of the arrays at each position
We perform the above step for 2 to 6. This has a complexity of O(6n), essentially O(n).

This can be further improved. Consider we check the first positions of both the arrays and find their values as 2 and 5 respectively. Then, we only need to check for 2 and 5 in the subsequent steps
This can be implememted using two for loops.
