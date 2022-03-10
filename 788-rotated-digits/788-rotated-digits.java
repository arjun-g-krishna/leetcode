class Solution {
    public int rotatedDigits(int n) {
              int[] arr=new int[n+1];
        int count=0;

        for(int i=0;i<=n;i++) {
            if (i <= 9) {
                if ((i == 0) || (i == 1) || (i == 8)) {
                    arr[i] = 0;
                } else if ((i == 2) || (i == 5) || (i == 6) || (i == 9)) {
                    arr[i] = 1;
                    count++;
                } else {
                    arr[i] = -1;
                }

            } else {
                int u = i % 10;
                int t = i / 10;

                if ((arr[u] == 0 && arr[t] == 1) || (arr[u] == 1 && arr[t] == 0)) {
                    arr[i] = 1;
                    count++;
                } else if (arr[u] == -1 || arr[t] == -1) {
                    arr[i] = -1;
                } else if (arr[u] == 0 && arr[t] == 0) {
                    arr[i] = 0;
                } else {
                    arr[i] = 1;
                    count++;
                }
            }

        }
      

        return count;
    }
}