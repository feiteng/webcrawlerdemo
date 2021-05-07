import java.io.*;
import java.util.*;

public class Solution{

    public String reformatDate(String date) {
        String[] split = date.split(" ");
        String[] month = {"", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};
        
        String day = split[0], mon = split[1], year = split[2];
        day = day.substring(0, day.length() - 2);
        if(day.length() < 2) day = "0" + day;
        int monInt = 0;
        for(int i = 1; i <= 12; i++)
        {
            if(month[i].equals(mon)) monInt = i;
        }
        String monthStr = "" + monInt;
        if(monthStr.length() < 2) monthStr = "0" + monthStr;
        return year + "-" + monthStr + "-" + day;
    }

    public int minCost(int n, int[] cuts) {
        Arrays.sort(cuts);
        for(int[] dd : dp)
        {
            Arrays.fill(dd, -1);
        }
        return cut(0, n, cuts, 0, cuts.length - 1);
    }
    
    int[][] dp = new int[110][110];
    
    int cut(int from, int to, int[] cuts, int cut_from, int cut_to)
    {
        if(cut_from > cut_to) return 0;
        if(dp[cut_from][cut_to] >= 0) return dp[cut_from][cut_to];
        
        int total = 1 << 30;
        for(int i = cut_from; i <= cut_to; i++)
        {
            if(cuts[i] < from || cuts[i] > to) continue;
            total = Math.min(total, to - from + 
                cut(from, cuts[i], cuts, cut_from, i - 1) + 
                cut(cuts[i], to, cuts, i + 1, cut_to));
        }
        return dp[cut_from][cut_to] = total;
    }        

    public int maxArea(int h, int w, int[] horizontalCuts, int[] verticalCuts) {
        List<Integer> hor = new ArrayList<>(), col = new ArrayList<>();
        hor.add(0);
        for(int hh : horizontalCuts) hor.add(hh);
        hor.add(h);
        col.add(0);
        for(int v : verticalCuts) col.add(v);
        col.add(w);
        Collections.sort(hor);
        Collections.sort(col);
        return calc(hor, col);
    }

    public String makeGood(String s) {
        Stack<Character> st = new Stack<>();
        for(char c : s.toCharArray())
        {
            if(!st.isEmpty() && 
               st.peek() != c && (
               Character.toUpperCase(st.peek()) == c || 
               Character.toLowerCase(st.peek()) == c                
               ))
            {
                st.pop();
            }
            else
            {
                st.push(c);
            }
        }
        StringBuilder sb = new StringBuilder();
        while(!st.isEmpty())
        {
            sb.append(st.pop());
        }
        return sb.reverse().toString();
    }

    
    public int numIdenticalPairs(int[] nums) {
        int re = 0;
        int n = nums.length;
        
        for(int i = 0; i < n; i++)
        {
            for(int j = i + 1; j < n; j++)
            {
                if(nums[i] == nums[j]) re++;
            }
        }
        return re;
    }

    String invert(String str)
    {
        int n = str.length();
        char[] c = new char[n];
        for(int i = 0; i < n; i++)
        {
            c[n - 1 - i] = str.charAt(i) == '0' ? '1' : '0';
        }
        return String.valueOf(c);
    }

    public char findKthBit(int n, int k) {
        String s = "0";
        while(n > 0)
        {
            s = s + "1" + invert(s);
            n--;
        }
        return s.charAt(k - 1);
    }
    
    

    
    int calc(List<Integer> l1, List<Integer> l2)
    {
        int m = l1.size(), n = l2.size();
        if(m > n) return calc(l2, l1);
        long dx = 0, dy = 0;
        long ans = 0;
        int mod = 1_000_000_007;
        for(int i = 0; i < m - 1; i++)
        {
            int curDx = l1.get(i + 1) - l1.get(i);
            dx = Math.max(dx, curDx);
        }
        for(int j = 0; j < n - 1; j++)
        {
            int curDy = l2.get(j + 1) - l2.get(j);
            dy = Math.max(dy, curDy);
        }
        
        return (int)(dx * dy % mod);
    }

    public int maxNonOverlapping(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        int sum = 0, re = 0, n = nums.length;
        
        map.put(0, 0);
        for(int i = 0; i < n; i++)
        {
            sum += nums[i];
            if(map.containsKey(sum - target))
            {
                re++;
                sum = 0;
                map = new HashMap<>();
                map.put(0, 0);
            }
            map.put(sum, 1);
        }
        return re;
    }    
        public int rangeSum(int[] nums, int n, int left, int right) {
        for(int i = 1; i < n; i++)
        {
            nums[i] += nums[i - 1];
        }
        
        List<Integer> list = new ArrayList<>();
        for(int i = 0; i < n; i++)
        {
            for(int j = i; j < n; j++)
            {
                int prev = i - 1 >= 0 ? nums[i - 1] : 0;
                list.add(nums[j] - prev);
            }
        }
        
        Collections.sort(list);
        // System.out.println(list);
        int sum = 0;
        for(int i = left - 1; i <= right - 1; i++)
        {
            sum += list.get(i);
        }
        return sum;
    }

    public int numSub(String s) {
        int i = 0;
        int j = 0;
        int n = s.length();
        int mod = 1_000_000_007;

        long re = 0;
        
        while(i < n)
        {
            while(i < n && s.charAt(i) == '0') {i++;}
            j = i;
            while(j < n && s.charAt(j) == '1') {j++;}
            int len = j - i;
            re += 1L * len * (len + 1) / 2;
            re %= mod;
            i = j;
        }
        return (int) re;
    }

        public int numSubseq(int[] nums, int target) {
        int n = nums.length;
        Arrays.sort(nums);
        int j = n - 1;
        long ans = 0, mod = 1_000_000_007;
        long[] pow = new long[1_000_10];
        pow[0] = 1;
        for(int i = 1; i <= 100_000; i++)
        {
            pow[i] = pow[i - 1] * 2 % mod;
        }
        for(int i = 0; i < n; i++)
        {
            while(j >= i && nums[i] + nums[j] > target) j--;
            if(j < i) break;
            int len = j - i;
            ans += pow[len];
        }
        return (int)(ans % mod);
    }

    double[] probs;
    public double maxProbability(int n, int[][] edges, double[] succProb, int start, int end) {
        probs = new double[n];
        Map<Integer, Map<Integer, Double>> map = new HashMap<>();
        for(int i = 0; i < n; i++) {map.put(i, new HashMap<>());}
        int len = edges.length;
        for(int i = 0; i < len; i++)
        {
            double p = succProb[i];
            int from = edges[i][0];
            int to = edges[i][1];
            map.get(to).put(from, p);
            map.get(from).put(to, p);
            
        }
        probs[start] = 1.0;
        return prob(start, end, map);
    }
    
    double prob(int from, int to, Map<Integer, Map<Integer, Double>> map)
    {
        double ans = 0.0;
        Queue<Double> prob = new LinkedList<>();
        Queue<Integer> q = new LinkedList<>();
        
        q.offer(from);
        prob.offer(1.0);
        while(!q.isEmpty())
        {
            double curProb = prob.poll();
            int cur = q.poll();
            
            for(int next : map.get(cur).keySet())
            {
                double nextProb = curProb * map.get(cur).get(next);
                if(probs[next] >= nextProb) continue;
                probs[next] = nextProb;
                q.offer(next);
                prob.offer(nextProb);
            }
        }
        return probs[to];
    }    

        public int minDifference(int[] nums) {
        int n = nums.length;
        if(n <= 4) return 0;
        Arrays.sort(nums);
        int d1 = nums[n - 4] - nums[0],
            d2 = nums[n - 3] - nums[1],
            d3 = nums[n - 2] - nums[2],
            d4 = nums[n - 1] - nums[3];
        return Math.min(Math.min(Math.min(d1, d2), d3), d4);
    }

        public int findMaxValueOfEquation(int[][] points, int k) {
        int n = points.length;
        int j = 0;
        Deque<int[]> q = new LinkedList<>();
        int maxi = Integer.MIN_VALUE;
        for(int i = 0; i < n; i++)
        {
            int xi = points[i][0];
            int yi = points[i][1];
            while(!q.isEmpty() && q.peekFirst()[0] + k < xi) q.pollFirst();
            if(!q.isEmpty()) maxi = Math.max(maxi, q.peekFirst()[1] + yi + xi);
            while(!q.isEmpty() && q.peekLast()[1] <= yi - xi) q.pollLast();
            q.offerLast(new int[]{xi, yi - xi});
        }
        return maxi;
    }

    public double getMinDistSum(int[][] positions) {
        double x = 0.0;
        double y = 0.0;
        int n = positions.length;
        for(int[] p : positions)
        {
            x += p[0];
            y += p[1];
        }
        x /= n;
        y /= n;
        
        double distance = distanceSum(x, y, positions);
        int k = 0;
        for(int i = 0; i < n; i++)
        {
            double nx = 1.0 * positions[i][0], 
                ny = 1.0 * positions[i][1];
            double newDistance = distanceSum(nx, ny, positions);
            if(newDistance < distance)
            {
                distance = newDistance;
                x = nx;
                y = ny;
            }
        }
        
        double test_distance = 1000.0, lower_limit = 0.000001;
        
        int[] dx = {1, 0, -1, 0}, dy = {0, 1, 0, -1};
        while(test_distance > lower_limit)
        {
            boolean found = false;
            for(int i = 0; i < 4; i++)
            {
                double nx = x + dx[i] * test_distance;
                double ny = y + dy[i] * test_distance;
                double newDistance = distanceSum(nx, ny, positions);
                if(newDistance < distance)
                {
                    distance = newDistance;
                    x = nx;
                    y = ny;
                    found = true;
                    break;
                }
            }
            if(!found) {test_distance /= 2;}
        }        
        
        return distance;
    }
    
    double distanceSum(double x, double y, int[][] pos)
    {
        double sum = 0;
        for(int[] p : pos)
        {
            double dx = x - p[0], dy = y - p[1];
            sum += Math.sqrt(dx * dx + dy * dy);
        }
        return sum;
    }    

        public boolean winnerSquareGame(int n) {
        boolean[][] f = new boolean[n + 1][2];
        f[1][0] = true;
        f[1][1] = true;
        for(int i = 2; i <= n; i++)
        {
            for(int j = 1; j * j <= i; j++)
            {
                f[i][0] |= !f[i - j * j][1];
                f[i][1] |= !f[i - j * j][0];
            }
        }
        
        return f[n][0];
    }

    

    class Point{
        double x;
        double y;
        Point(double X,double Y){
            x = X;
            y = Y;
        }
        
        double atan(){
            return Math.atan2(y,x);
        }
        double length() {
            return Math.sqrt(x*x+y*y+1e-7);
        }
        Point add(Point Q) {
            return new Point(x+Q.x,y+Q.y);
        }
        Point sub(Point Q) {
            return new Point(x-Q.x,y-Q.y);
        }
        Point mul(double d) {
            return new Point(x*d,y*d);
        }
        Point div(double d) {
            return new Point(x/d,y/d);
        }
        
    }


    class Triangle{
        double eps = 1e-7;
        Point A;
        Point B;
        Point C;
        double edgeA;
        double edgeB;
        double edgeC;
        double argA;
        double argB;
        double argC;
        Triangle(Point a,Point b,Point c){
            A = a;
            B = b;
            C = c;
            edgeA = b.sub(c).length();
            edgeB = c.sub(a).length();
            edgeC = a.sub(b).length();
            argA = Math.acos(getcos(edgeA,edgeB,edgeC));
            argB = Math.acos(getcos(edgeB,edgeC,edgeA));
            argC = Math.acos(getcos(edgeC,edgeA,edgeB));
        }
        double getcos(double a,double b,double c){
            return (b*b+c*c-a*a)/(2*b*c);
        }
        Point outheart() {
            return A.mul(Math.sin(2*argA)).add(B.mul(Math.sin(2*argB))).add(C.mul(Math.sin(2*argC))).div(Math.sin(2*argA)+Math.sin(2*argB)+Math.sin(2*argC));
        }
    }

    class Slidemax{
        int[] dat;
        
        ArrayDeque<LongIntPair> q = new ArrayDeque<LongIntPair>();
        
        long get() {
            if(q.isEmpty()) return (long) -1e17;
            return q.peek().a;
        }
        
        void remove() {
            q.getFirst().b--;
            if(q.getFirst().b==0)q.pollFirst();
        }
        
        void add(long x) {
            int num = 1;
            while(!q.isEmpty()&&q.peekLast().a<=x) {
                num += q.peekLast().b;
                q.pollLast();
            }
            q.addLast(new LongIntPair(x,num));
        }
    }
    class Slidemin{
        int[] dat;
        int l = 0;
        int r = -1;
        ArrayDeque<LongIntPair> q = new ArrayDeque<LongIntPair>();
        
        long get() {
            if(q.isEmpty()) return (long)1e17;
            return q.peek().a;
        }
        
        void remove() {
            q.getFirst().b--;
            if(q.getFirst().b==0)q.pollFirst();
        }
        
        void add(long x) {
            int num = 1;
            while(!q.isEmpty()&&q.peekLast().a>=x) {
                num += q.peekLast().b;
                q.pollLast();
            }
            q.addLast(new LongIntPair(x,num));
        }
    }


    class Counter{
        
        int[] cnt;
        Counter(int M){
            cnt = new int[M+1];
        }
        Counter(int M,int[] A){
            cnt = new int[M+1];
            for(int i=0;i<A.length;i++)add(A[i]);
        }
        void add(int e) {
            cnt[e]++;
        }
        void remove(int e) {
            cnt[e]--;
        }
        int count(int e) {
            return cnt[e];
        }
    }

    class MultiHashSet{
        HashMap<Integer,Integer> set;
        int size;
        long sum;
        MultiHashSet(){
            set = new HashMap<Integer,Integer>();
            size = 0;
            sum = 0;
        }
        void add(int e){
            if(set.containsKey(e))set.put(e,set.get(e)+1);
            else set.put(e,1);
            size++;
            sum += e;
        }
        void remove(int e) {
            set.put(e,set.get(e)-1);
            if(set.get(e)==0)set.remove(e);
            size--;
            sum -= e;
        }
        
        boolean contains(int e) {
            return set.containsKey(e);
        }
        boolean isEmpty() {
            return set.isEmpty();
        }
        int count(int e) {
            if(contains(e))return set.get(e);
            else return 0;
        }
        
        Set<Integer> keyset(){
            return set.keySet();
        }

    }


    class MultiSet{
        TreeMap<Integer,Integer> set;
        long size;
        long sum;
        MultiSet(){
            set = new TreeMap<Integer,Integer>();
            size = 0;
            sum = 0;
        }
        void add(int e){
            if(set.containsKey(e))set.put(e,set.get(e)+1);
            else set.put(e,1);
            size++;
            sum += e;
        }
        void addn(int e,int n){
            if(set.containsKey(e))set.put(e,set.get(e)+n);
            else set.put(e,n);
            size += n;
            sum += e*(long)n;
        }
        void remove(int e) {
            set.put(e,set.get(e)-1);
            if(set.get(e)==0)set.remove(e);
            size--;
            sum -= e;
        }
        int first() {return set.firstKey();}
        int last() {return set.lastKey();}
        int lower(int e) {return set.lowerKey(e);}
        int higher(int e) {return set.higherKey(e);}
        int floor(int e) {return set.floorKey(e);}
        int ceil(int e) {return set.ceilingKey(e);}
        boolean contains(int e) {return set.containsKey(e);}
        boolean isEmpty() {return set.isEmpty();}
        int count(int e) {
            if(contains(e))return set.get(e);
            else return 0;
        }
        MultiSet marge(MultiSet T) {
            if(size>T.size) {
                while(!T.isEmpty()) {
                    add(T.first());
                    T.remove(T.first());
                }
                return this;
            }else {
                while(!isEmpty()) {
                    T.add(first());
                    remove(first());
                }
                return T;
            }
        }
        Set<Integer> keyset(){
            return set.keySet();
        }

    }

    class MultiSetL{
        TreeMap<Long,Integer> set;
        int size;
        long sum;
        MultiSetL(){
            set = new TreeMap<Long,Integer>();
            size = 0;
            sum = 0;
        }
        void add(long e){
            if(set.containsKey(e))set.put(e,set.get(e)+1);
            else set.put(e,1);
            size++;
            sum += e;
        }
        void remove(long e) {
            set.put(e,set.get(e)-1);
            if(set.get(e)==0)set.remove(e);
            size--;
            sum -= e;
        }
        long first() {return set.firstKey();}
        long last() {return set.lastKey();}
        long lower(long e) {return set.lowerKey(e);}
        long higher(long e) {return set.higherKey(e);}
        long floor(long e) {return set.floorKey(e);}
        long ceil(long e) {return set.ceilingKey(e);}
        boolean contains(long e) {return set.containsKey(e);}
        boolean isEmpty() {return set.isEmpty();}
        int count(long e) {
            if(contains(e))return set.get(e);
            else return 0;
        }
        MultiSetL marge(MultiSetL T) {
            if(size>T.size) {
                while(!T.isEmpty()) {
                    add(T.first());
                    T.remove(T.first());
                }
                return this;
            }else {
                while(!isEmpty()) {
                    T.add(first());
                    remove(first());
                }
                return T;
            }
        }
        Set<Long> keyset(){
            return set.keySet();
        }
    }



    class BetterGridGraph{
        int N;
        int M;
        char[][] S;
        HashMap<Character,ArrayList<Integer>> map;
        int[] dx = {0,1,0,-1};
        int[] dy = {1,0,-1,0};
        char w;
        char b = '#';
        BetterGridGraph(int n,int m,String[] s,char[] c){

            N = n;
            M = m;
            for(int i=0;i<s.length;i++) {
                S[i] = s[i].toCharArray();
            }
            map = new HashMap<Character,ArrayList<Integer>>();
            for(int i=0;i<c.length;i++) {
                map.put(c[i],new ArrayList<Integer>());
            }
            for(int i=0;i<n;i++) {
                for(int j=0;j<m;j++) {
                    for(int k=0;k<c.length;k++) {
                        if(S[i][j]==c[k])map.get(c[k]).add(toint(i,j));
                    }
                }
            }
        }
        BetterGridGraph(int n,int m,char[][] s,char[] c){

            N = n;
            M = m;
            S = s;
            map = new HashMap<Character,ArrayList<Integer>>();
            for(int i=0;i<c.length;i++) {
                map.put(c[i],new ArrayList<Integer>());
            }
            for(int i=0;i<n;i++) {
                for(int j=0;j<m;j++) {
                    for(int k=0;k<c.length;k++) {
                        if(S[i][j]==c[k])map.get(c[k]).add(toint(i,j));
                    }
                }
            }
        }

        BetterGridGraph(int n,int m,String[] s,char[] c,char W,char B){

            N = n;
            M = m;
            for(int i=0;i<s.length;i++) {
                S[i] = s[i].toCharArray();
            }
            w = W;
            b = B;
            map = new HashMap<Character,ArrayList<Integer>>();
            for(int i=0;i<c.length;i++) {
                map.put(c[i],new ArrayList<Integer>());
            }
            for(int i=0;i<n;i++) {
                for(int j=0;j<m;j++) {
                    for(int k=0;k<c.length;k++) {
                        if(S[i][j]==c[k])map.get(c[k]).add(toint(i,j));
                    }
                }
            }
        }
        BetterGridGraph(int n,int m,char[][] s,char[] c,char W,char B){

            N = n;
            M = m;
            S = s;
            w = W;
            b = B;
            map = new HashMap<Character,ArrayList<Integer>>();
            for(int i=0;i<c.length;i++) {
                map.put(c[i],new ArrayList<Integer>());
            }
            for(int i=0;i<n;i++) {
                for(int j=0;j<m;j++) {
                    for(int k=0;k<c.length;k++) {
                        if(S[i][j]==c[k])map.get(c[k]).add(toint(i,j));
                    }
                }
            }
        }

        int toint(int i,int j) {
            return i*M+j;
        }
        
        ArrayList<Integer> getposlist(char c) {
            return map.get(c);
        }
        
        int getpos(char c) {
            return map.get(c).get(0);
        }

        int[] bfs(char C) {
            int[] L = new int[N*M];
            ArrayDeque<Integer> Q = new ArrayDeque<Integer>();
            for(int i=0;i<N*M;i++){
                L[i] = -1;
            }
            for(int s:map.get(C)) {
                L[s] = 0;
                Q.add(s);
            }
            Range X = new Range(0,N-1);
            Range Y = new Range(0,M-1);
            while(!Q.isEmpty()){
                int v = Q.poll();
                for(int i=0;i<4;i++){
                    int x = v/M;
                    int y = v%M;
                    int nx = x+dx[i];
                    int ny = y+dy[i];
                    if(X.isIn(nx)&&Y.isIn(ny)&&S[nx][ny]!=b) {
                        int w = toint(nx,ny);
                        if(L[w]==-1){
                            L[w] = L[v] + 1;
                            Q.add(w);
                        }
                    }
                }
            }
            return L;
        }
        
        int[] bfsb(int s) {
            int[] L = new int[N*M];
            ArrayDeque<Integer> Q = new ArrayDeque<Integer>();
            for(int i=0;i<N*M;i++){
                L[i] = -1;
            }
            Q.add(s);
            L[s] = 0;
            Range X = new Range(0,N-1);
            Range Y = new Range(0,M-1);
            while(!Q.isEmpty()){
                int v = Q.poll();
                for(int i=0;i<4;i++){
                    int x = v/M;
                    int y = v%M;
                    int nx = x+dx[i];
                    int ny = y+dy[i];
                    if(X.isIn(nx)&&Y.isIn(ny)) {
                        int w = toint(nx,ny);
                        if(L[w]==-1){
                            if(S[x][y]==S[nx][ny]) {
                                L[w] = L[v];
                                Q.addFirst(w);
                            }else {
                                L[w] = L[v] + 1;
                                Q.addLast(w);
                            }
                        }
                    }
                }
            }
            return L;
        }

        
    }
    class IntGridGraph{
        int N;
        int M;
        int[][] B;
        int[] dx = {0,1,0,-1};
        int[] dy = {1,0,-1,0};
        BiFunction<Integer,Integer,Boolean> F;
        
        IntGridGraph(int n,int m,int[][] b){

            N = n;
            M = m;
            B = b;
        }
        IntGridGraph(int n,int m,int[][] b,BiFunction<Integer,Integer,Boolean> f){

            N = n;
            M = m;
            B = b;
            F = f;
        }
        
            
        int toint(int i,int j) {
            return i*M+j;
        }
        

        int[] bfs(int s) {
            int[] L = new int[N*M];
            for(int i=0;i<N*M;i++){
                L[i] = -1;
            }
            L[s] = 0;
            ArrayDeque<Integer> Q = new ArrayDeque<Integer>();
            Q.add(s);
            Range X = new Range(0,N-1);
            Range Y = new Range(0,M-1);
            while(!Q.isEmpty()){
                int v = Q.poll();
                for(int i=0;i<4;i++){
                    int x = v/M;
                    int y = v%M;
                    int nx = x+dx[i];
                    int ny = y+dy[i];
                    if(X.isIn(nx)&&Y.isIn(ny)&&F.apply(B[x][y],B[nx][ny])) {
                    int w = toint(nx,ny);                        
                        if(L[w]==-1){
                            L[w] = L[v] + 1;
                            Q.add(w);
                        }
                    }
                }
            }
            return L;
        }
        
        void bfs(int s,int[] L) {
            
            if(L[s]!=-1) return;
            L[s] = 0;
            ArrayDeque<Integer> Q = new ArrayDeque<Integer>();
            Q.add(s);
            Range X = new Range(0,N-1);
            Range Y = new Range(0,M-1);
            while(!Q.isEmpty()){
                int v = Q.poll();
                for(int i=0;i<4;i++){
                    int x = v/M;
                    int y = v%M;
                    int nx = x+dx[i];
                    int ny = y+dy[i];
                    if(X.isIn(nx)&&Y.isIn(ny)&&F.apply(B[x][y],B[nx][ny])) {
                    int w = toint(nx,ny);                        
                        if(L[w]==-1){
                            L[w] = L[v] + 1;
                            Q.add(w);
                        }
                    }
                }
            }
            return;
        }

       
    }

    class Trie{
        int nodenumber = 1;
        ArrayList<TrieNode> l;
        Trie(){
            l = new ArrayList<TrieNode>();
            l.add(new TrieNode());
        }

        void add(String S,int W){
            int now = 0;
            for(int i=0;i<S.length();i++) {
                TrieNode n = l.get(now);
                char c = S.charAt(i);
                if(n.Exist[c-'a']!=-1) {
                    now = n.Exist[c-'a'];
                }else {
                    l.add(new TrieNode());
                    n.Exist[c-'a'] = nodenumber;
                    now = nodenumber;
                    nodenumber++;
                }
            }
            l.get(now).weight = W;
        }

        void find(String S,int i,int[] dp) {
            int now = 0;
            dp[i+1] = Math.max(dp[i],dp[i+1]);
            for(int j=0;;j++) {
                TrieNode n = l.get(now);
                dp[i+j] = Math.max(dp[i+j],dp[i]+n.weight);
                int slook = i+j;
                if(slook>=S.length())return;
                char c = S.charAt(slook);
                if(n.Exist[c-'a']==-1)return;
                now = n.Exist[c-'a'];
            }
        }
    }

    class TrieNode{

        int[] Exist = new int[26];
        int weight = 0;
        TrieNode(){
            for(int i=0;i<26;i++) {
                Exist[i] = -1;
            }
        }
    }

    class SizeComparator implements Comparator<Edge>{
        int[] size;
        SizeComparator(int[] s) {
            size = s;
        }

        public int compare(Edge o1, Edge o2) {
            return size[o1.to]-size[o2.to];

        }

    }

    class ConvexHullTrick {
        long[] A, B;
        int len;

        public ConvexHullTrick(int n) {
            A = new long[n];
            B = new long[n];
        }

        private boolean check(long a, long b) {
            return (B[len - 2] - B[len - 1]) * (a - A[len - 1]) >= (B[len - 1] - b) * (A[len - 1] - A[len - 2]);
        }

        public void add(long a, long b) {
            while (len >= 2 && check(a, b)) {
                len--;
            }
            A[len] = a;
            B[len] = b;
            len++;
        }

        public long query(long x) {
            int l = -1, r = len - 1;
            while (r - l > 1) {
                int mid = (r + l) / 2;
                if (get(mid,x)>=get(mid+1,x)) {
                    l = mid;
                } else {
                    r = mid;
                }
            }
            return get(r,x);
        }

        private long get(int k, long x) {
            return A[k] * x + B[k];
        }
    }

    class Range{
        long l;
        long r;
        long length;
        Range(int L,int R){
            l = L;
            r = R;
            length = R-L+1;
        }

        public Range(long L, long R) {
            l = L;
            r = R;
            length = R-L+1;
        }

        boolean isIn(int x) {
            return (l<=x&&x<=r);

        }
        long kasanari(Range S) {
            if(this.r<S.l||S.r<this.l) return 0;
            else return Math.min(this.r,S.r) - Math.max(this.l,S.l)+1;
        }
    }
    class LeftComparator implements Comparator<Range>{
        public int compare(Range P, Range Q) {
            return (int) Math.signum(P.l-Q.l);
        }
    }
    class RightComparator implements Comparator<Range>{
        public int compare(Range P, Range Q) {
            return (int) Math.signum(P.r-Q.r);
                    
        }
    }
    class LengthComparator implements Comparator<Range>{
        public int compare(Range P, Range Q) {
            return (int) Math.signum(P.length-Q.length);
        }
    }
    class SegmentTree<T,E>{
        int N;
        BiFunction<T,T,T> f;
        BiFunction<T,E,T> g;
        T d1;
        ArrayList<T> dat;
        SegmentTree(BiFunction<T,T,T> F,BiFunction<T,E,T> G,T D1,T[] v){
            int n = v.length;
            f = F;
            g = G;
            d1 = D1;
            init(n);
            build(v);
        }


        void init(int n) {
            N = 1;
            while(N<n)N*=2;
            dat = new ArrayList<T>();
        }

        void build(T[] v) {
            for(int i=0;i<2*N;i++) {
                dat.add(d1);
            }
            for(int i=0;i<v.length;i++) {
                dat.set(N+i-1,v[i]);
            }
            for(int i=N-2;i>=0;i--) {
                dat.set(i,f.apply(dat.get(i*2+1),dat.get(i*2+2)));
            }
        }

        void update(int k,E a) {
            k += N-1;
            dat.set(k,g.apply(dat.get(k),a));
            while(k>0){
                k = (k-1)/2;
                dat.set(k,f.apply(dat.get(k*2+1),dat.get(k*2+2)));
            }
        }

        T query(int a,int b, int k, int l ,int r) {
            if(r<=a||b<=l) return d1;
            if(a<=l&&r<=b) return dat.get(k);
            T vl = query(a,b,k*2+1,l,(l+r)/2);
            T vr = query(a,b,k*2+2,(l+r)/2,r);
            return f.apply(vl,vr);
        }
        T query(int a,int b){
            return query(a,b,0,0,N);
        }

    }

    class LazySegmentTree<T,E> extends SegmentTree<T,E>{
        BiFunction<E,E,E> h;
        BiFunction<E,Integer,E> p = (E a,Integer b) ->{return a;};
        E d0;
        ArrayList<E> laz;
        LazySegmentTree(BiFunction<T,T,T> F,BiFunction<T,E,T> G,BiFunction<E,E,E> H,T D1,E D0,T[] v){
            super(F,G,D1,v);
            int n = v.length;
            h = H;
            d0 = D0;
            Init(n);
        }
        void build() {

        }
        void Init(int n){
            laz = new ArrayList<E>();
            for(int i=0;i<2*N;i++) {
                laz.add(d0);
            }
        }

        void eval(int len,int k) {
            if(laz.get(k).equals(d0)) return;
            if(k*2+1<N*2-1) {
                laz.set(k*2+1,h.apply(laz.get(k*2+1),laz.get(k)));
                laz.set(k*2+2,h.apply(laz.get(k*2+2),laz.get(k)));
            }
            dat.set(k,g.apply(dat.get(k), p.apply(laz.get(k), len)));
            laz.set(k,d0);
        }

        T update(int a,int b,E x,int k,int l,int r) {
            eval(r-l,k);
            if(r<=a||b<=l) {
                return dat.get(k);
            }
            if(a<=l&&r<=b) {
                laz.set(k,h.apply(laz.get(k),x));
                return g.apply(dat.get(k),p.apply(laz.get(k),r-l));
            }
            T vl = update(a,b,x,k*2+1,l,(l+r)/2);
            T vr = update(a,b,x,k*2+2,(l+r)/2,r);
            dat.set(k,f.apply(vl,vr));
            return dat.get(k);

        }

        T update(int a,int b,E x) {
            return update(a,b,x,0,0,N);
        }

        T query(int a,int b,int k,int l,int r) {
            
            eval(r-l,k);
            if(r<=a||b<=l) return d1;
            if(a<=l&&r<=b) return dat.get(k);
            T vl = query(a,b,k*2+1,l,(l+r)/2);
            T vr = query(a,b,k*2+2,(l+r)/2,r);
            return f.apply(vl, vr);
        }

        T query(int a,int b){
            return query(a,b,0,0,N);
        }

    }

    class AddSumSegmentTree{
        int N;
        int d1;
        ArrayList<Integer> dat;
        AddSumSegmentTree(int[] v){
            int n = v.length;
            init(n);
            build(v);
        }

        void init(int n) {
            N = 1;
            while(N<n)N*=2;
            dat = new ArrayList<Integer>();
        }

        void build(int[] v) {
            for(int i=0;i<2*N;i++) {
                dat.add(d1);
            }
            for(int i=0;i<v.length;i++) {
                dat.set(N+i-1,v[i]);
            }
            for(int i=N-2;i>=0;i--) {
                dat.set(i,dat.get(i*2+1)+dat.get(i*2+2));
            }
        }

        void update(int k,int a) {
            k += N-1;
            dat.set(k,dat.get(k)+a);
            while(k>0){
                k = (k-1)/2;
                dat.set(k,dat.get(k*2+1)+dat.get(k*2+2));
            }
        }

        int query(int a,int b, int k, int l ,int r) {
            if(r<=a||b<=l) return d1;
            if(a<=l&&r<=b) return dat.get(k);
            int vl = query(a,b,k*2+1,l,(l+r)/2);
            int vr = query(a,b,k*2+2,(l+r)/2,r);
            return vl+vr;
        }
        int query(int a,int b){
            return query(a,b,0,0,N);
        }
    }
    class AddSumLazySegmentTree {
        int N;
        long[] dat;
        long[] laz;
        AddSumLazySegmentTree(long[] v){
            init(v.length);

            for(int i=0;i<v.length;i++) {
                dat[N+i-1]=v[i];
            }
            for(int i=N-2;i>=0;i--) {
                dat[i]=dat[i*2+1]+dat[i*2+2];
            }
        }

        void init(int n) {
            N = 1;
            while(N<n)N*=2;
            dat = new long[2*N];
            laz = new long[2*N];
        }


        void eval(int len,int k) {
            if(laz[k]==0) return;
            if(k*2+1<N*2-1) {
                laz[k*2+1] += laz[k];
                laz[k*2+2] += laz[k];
            }
            dat[k] += laz[k] * len;
            laz[k] = 0;
        }

        long update(int a,int b,long x,int k,int l,int r) {
            eval(r-l,k);
            if(r<=a||b<=l) {
                return dat[k];
            }
            if(a<=l&&r<=b) {
                laz[k] += x;
                return dat[k]+laz[k]*(r-l);
            }
            long vl = update(a,b,x,k*2+1,l,(l+r)/2);
            long vr = update(a,b,x,k*2+2,(l+r)/2,r);
            return dat[k] = vl+vr;


        }

        long update(int a,int b,long x) {
            return update(a,b,x,0,0,N);
        }

        long query(int a,int b,int k,int l,int r) {
            eval(r-l,k);
            if(r<=a||b<=l) return 0;
            if(a<=l&&r<=b) return dat[k];

            long vl = query(a,b,k*2+1,l,(l+r)/2);
            long vr = query(a,b,k*2+2,(l+r)/2,r);
            return vl+vr;
        }

        long query(int a,int b){
            return query(a,b,0,0,N);
        }

    }

    class BinaryIndexedTree{
        int[] val;
        BinaryIndexedTree(int N){
            val = new int[N+1];
        }
        long sum(int i) {
            if(i==0)return 0;
            long s = 0;
            while(i>0) {
                s += val[i];
                i -= i & (-i);
            }
            return s;
        }
        void add(int i,int x) {
            if(i==0)return;
            while(i<val.length){
                val[i] += x;
                i += i & (-i);
            }
        }
    }


    class UnionFindTree {
        int[] root;
        int[] rank;
        long[] size;
        int[] edge;
        int num;
        UnionFindTree(int N){
            root = new int[N];
            rank = new int[N];
            size = new long[N];
            edge = new int[N];
            num = N;
            for(int i=0;i<N;i++){
                root[i] = i;
                size[i] = 1;
            }
        }
        public long size(int x) {
            return size[find(x)];
        }
        public boolean isRoot(int x) {
            return x==find(x);
        }
        public long extraEdge(int x) {
            int r = find(x);
            return edge[r] - size[r] + 1;
        }
        public int find(int x){
            if(root[x]==x){
                return x;
            }else{
                return find(root[x]);
            }
        }

        public boolean unite(int x,int y){
            x = find(x);
            y = find(y);
            if(x==y){
                edge[x]++;
                return false;
            }else{
                num--;
                if(rank[x]<rank[y]){
                    root[x] = y;
                    size[y] += size[x];
                    edge[y] += edge[x]+1;
                }else{
                    root[y] = x;
                    size[x] += size[y];
                    edge[x] += edge[y]+1;
                    if(rank[x]==rank[y]){
                        rank[x]++;
                    }
                }
                return true;
            }
        }

        public boolean same(int x,int y){
            return find(x)==find(y);
        }

    }
    class LightUnionFindTree {
        int[] par;
        int num;
        LightUnionFindTree(int N){
            par = new int[N];
            num = N;
            for(int i=0;i<N;i++){
                par[i] = -1;
            }
        }
        public boolean isRoot(int x) {
            return x==find(x);
        }
        
        public int find(int x){
            if(par[x]<0){
                return x;
            }else{
                return find(par[x]);
            }
        }

        public void unite(int x,int y){
            x = find(x);
            y = find(y);
            if(x==y){
                return;
            }else{
                num--;
                if(par[x]<par[y]){
                    par[x] += par[y];
                    par[y] = x;
                }else{
                    par[y] += par[x];
                    par[x] = y;
                }
            }
        }

        public boolean same(int x,int y){
            return find(x)==find(y);
        }

    }

    class ParticalEternalLastingUnionFindTree extends UnionFindTree{
        int[] time;
        int now;
        ParticalEternalLastingUnionFindTree(int N){
            super(N);
            time = new int[N];
            for(int i=0;i<N;i++) {
                time[i] = 1000000007;
            }
        }

        public int find(int t,int i) {
            if(time[i]>t) {
                return i;
            }else {
                return find(t,root[i]);
            }
        }

        public void unite(int x,int y,int t) {
            now = t;
            x = find(t,x);
            y = find(t,y);
            if(x==y)return;
            if(rank[x]<rank[y]){
                root[x] = y;
                size[y] += size[x];
                time[x] = t;
            }else{
                root[y] = x;
                size[x] += size[y];
                if(rank[x]==rank[y]){
                    rank[x]++;
                }
                time[y] = t;
            }
        }

        public int sametime(int x,int y) {
            if(find(now,x)!=find(now,y)) return -1;
            int ok = now;
            int ng = 0;
            while(ok-ng>1) {
                int mid = (ok+ng)/2;
                if(find(mid,x)==find(mid,y)) {
                    ok = mid;
                }else {
                    ng = mid;
                }
            }
            return ok;
        }


    }
    class FlowEdge{
        int to;
        long cap;
        int rev = 0;
        FlowEdge(int To,long Cap,int Rev){
            to = To;
            cap = Cap;
            rev = Rev;
        }
    }
    class FlowGraph{
        ArrayList<FlowEdge>[] list;
        int[] level;
        int[] iter;
        ArrayDeque<Integer> q;
        FlowGraph(int N){
            list = new ArrayList[N];
            for(int i=0;i<N;i++) {
                list[i] = new ArrayList<FlowEdge>();
            }
            level = new int[N];
            iter = new int[N];
            q = new ArrayDeque<Integer>();
        }
        
        void addEdge(int i, int to, long cap) {
            list[i].add(new FlowEdge(to,cap,list[to].size()));
            list[to].add(new FlowEdge(i,0,list[i].size()-1));
        }
        
        void bfs(int s) {
            Arrays.fill(level,-1);
            level[s] = 0;
            q.add(s);
            while(!q.isEmpty()) {
                int v = q.poll();
                for(FlowEdge e:list[v]) {
                    if(e.cap>0&&level[e.to]<0) {
                        level[e.to] = level[v] + 1;
                        q.add(e.to);
                    }
                }
            }
        }
        
        long dfs(int v,int t,long f) {
            if(v==t) return f;
            for(int i = iter[v];i<list[v].size();i++) {
                FlowEdge e = list[v].get(i);
                if(e.cap>0&&level[v]<level[e.to]) {
                    long d = dfs(e.to,t,Math.min(f,e.cap));
                    if(d>0) {
                        e.cap -= d;
                        list[e.to].get(e.rev).cap += d;
                        return d;
                    }
                }
                iter[v]++;
            }
            return 0;
        }
        
        long flow(int s,int t,long lim) {
            long flow = 0;
            while(true) {
                bfs(s);
                if(level[t]<0||lim==0) return flow;
                Arrays.fill(iter,0);
                while(true) {
                    long f = dfs(s,t,lim);
                    if(f>0) {
                        flow += f;
                        lim -= f;
                    }
                    
                    else break;
                }
            }
            
        }
        long flow(int s,int t) {
            return flow(s,t,1000000007);
        }
    }


    class LightGraph {
        ArrayList<Integer>[] list;
        int size;
        TreeSet<LinkEdge> Edges = new TreeSet<LinkEdge>(new LinkEdgeComparator());

        @SuppressWarnings("unchecked")
        LightGraph(int N){
            size = N;
            list = new ArrayList[N];
            for(int i=0;i<N;i++){
                list[i] = new ArrayList<Integer>();
            }
        }

        




        void addEdge(int a,int b){
            list[a].add(b);
        }

        
        public Stack<Integer> findCycle() {
            Stack<Integer> ans = new Stack<Integer>();
            boolean[] v = new boolean[size];
            boolean[] f = new boolean[size];
            for(int i=0;i<size;i++) {
                if(findCycle(i,ans,v,f))break;
            }
            return ans;
        }
        private boolean findCycle(int i, Stack<Integer>ans, boolean[] v,boolean[] f) {
            v[i] = true;
            ans.push(i);
            for(int e:list[i]) {
                if(f[e]) continue;
                if(v[e]&&!f[e]) {
                    return true;
                }
                if(findCycle(e,ans,v,f))return true;
            }
            ans.pop();
            f[i] = true;
            return false;
            
        }
        
    }


    class LinkEdge{
        long L;
        int a ;
        int b;
        int id;
        LinkEdge(long l,int A,int B){
            L = l;
            a = A;
            b = B;
        }
        LinkEdge(long l,int A,int B,int i){
            L = l;
            a = A;
            b = B;
            id = i;
        }
        public boolean equals(Object o){
            LinkEdge O = (LinkEdge) o;
            return O.a==this.a&&O.b==this.b&&O.L==this.L;
        }

        public int hashCode(){
            return Objects.hash(L,a,b);
        }
    }

    class DoubleLinkEdge{
        double D;
        int a;
        int b;
        DoubleLinkEdge(double d,int A,int B){
            D = d;
            a = A;
            b = B;
        }
        public boolean equals(Object o){
            DoubleLinkEdge O = (DoubleLinkEdge) o;
            return O.a==this.a&&O.b==this.b&&O.D==this.D;
        }
     
        public int hashCode(){
            return Objects.hash(D,a,b);
        }
    }
     

    class Edge{
        int to;
        long cost;
        Edge(int a,long b){
            to = a;
            cost = b;
        }
    }

    class indexedEdge extends Edge{
        int id;
        indexedEdge(int a, long b, int c) {
            super(a,b);
            id = c;
        }
        
    }

    class DoubleLinkEdgeComparator implements Comparator<DoubleLinkEdge>{
        public int compare(DoubleLinkEdge P, DoubleLinkEdge Q) {
            return Double.compare(P.D,Q.D);
        }
    }

    class LinkEdgeComparator implements Comparator<LinkEdge>{
        public int compare(LinkEdge P, LinkEdge Q) {
            return Long.compare(P.L,Q.L);
        }
    }


    class Pair{
        long a;
        long b;

        Pair(long p,long q){
            this.a = p;
            this.b = q;
        }

        public boolean equals(Object o){
            Pair O = (Pair) o;
            return O.a==this.a&&O.b==this.b;
        }

        public int hashCode(){
            return Objects.hash(a,b);
        }
    }

    class SampleComparator implements Comparator<Pair>{
        public int compare(Pair P, Pair Q) {
            long t = P.a-Q.a;
            if(t==0){
                if(P.b==Q.b)return 0;
                return P.b>Q.b?1:-1;

            }
            return t>=0?1:-1;
        }
    }


    class LongIntPair{
        long a;
        int b;

        LongIntPair(long p,int q){
            this.a = p;
            this.b = q;
        }

        public boolean equals(Object o){
            LongIntPair O = (LongIntPair) o;
            return O.a==this.a&&O.b==this.b;

        }

        public int hashCode(){
            return Objects.hash(a,b);
        }
    }

    class LongIntComparator implements Comparator<LongIntPair>{
        public int compare(LongIntPair P, LongIntPair Q) {
            long t = P.a-Q.a;
            if(t==0){
                if(P.b>Q.b){
                    return 1;
                }else{
                    return -1;
                }
            }
            return t>=0?1:-1;
        }
    }

}