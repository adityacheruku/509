class Solution {
    public static void main(String[] args) {
        String  str = "()";
        int n = str.length();
        int i=0;
        int flag = 0;
        while(i<n){
            if(str.charAt(i)=='('||str.charAt(i)=='{'||str.charAt(i)=='['){
                char m = str.charAt(i);
                
                switch(m){
                    case '(':  
                        flag = (str.charAt(i+1)==')') ? 1 : 0;
                    case '{':  
                        flag= (str.charAt(i+1)=='}') ? 1 : 0;
                     case '[':  
                        flag = (str.charAt(i+1)=='[') ? 1 : 0;

                }
                i++;
            }
        }
        if(flag==1){
            System.out.println("true");
        }
        else
            System.out.println("tr");     
       
    }
}