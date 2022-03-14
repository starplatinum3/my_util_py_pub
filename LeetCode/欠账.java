public static int getIndex2(String str, String aim){
        if(str == null || aim == null || str.length() < aim.length()) return -1;
        for(int i = 0; i <= str.length() - aim.length(); i++)
        {
            if(isCountEqual(str, i, aim)) return i;
        }
        return -1;
    }
    public static boolean isCountEqual(String str, int lift, String aim){
        int[] count = new int[256];
        for(int i = 0; i < aim.length(); i++){
            count[aim.charAt(i)] ++;
        }
        for(int i = 0; i < aim.length(); i++){
            // 为什么是 ==0  而不是 <0 
            if(count[str.charAt(lift + i)]-- == 0) return false;
        }
        return true;
    }

    // https://www.cnblogs.com/unknown6248/p/14457069.html