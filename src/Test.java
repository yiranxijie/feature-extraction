import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;


public class Test {  
    public static void main(String args[]) throws IOException{  
        Process process = null;  
        try {  
              
            //1----解压  
            //apktool路径  
            String path = "C:\\Windows";  
            //保存路径  
            String appPath = "D:\\tao\\";  
            File file =new File(path);  
              
            process = Runtime.getRuntime().exec("cmd.exe /c apktool d -f "+appPath+"91.apk -o "+appPath+"test\\apktest",null,file);  
            if(process.waitFor()!=0)System.out.println("解压失败。。。");  
              
        }catch (Exception e)  
        {  
            e.printStackTrace();  
        } 
    }  
}