import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.zip.ZipEntry;
import java.util.zip.ZipFile;
import java.util.zip.ZipInputStream;


public class GetClasses_dex {

	    public static void main(String[] args) throws Exception {
	        try {  
	               readZipFile("D:\\CoolWeather.apk");  
	           } catch (Exception e) {  
	               e.printStackTrace();  
	           }  
	    }
	    
	    public static void readZipFile(String path) throws Exception {  
	           ZipFile zf = new ZipFile(path);  
	           InputStream in = new BufferedInputStream(new FileInputStream(path));  
	           ZipInputStream zin = new ZipInputStream(in);  
	           ZipEntry ze;  
	           OutputStreamWriter osw =null;
	           String src=path.split(":")[0]+":\\test";
	           while ((ze = zin.getNextEntry()) != null) {  
	               if (ze.isDirectory()) {
	               } else {  
	                   System.err.println("file - " + ze.getName() + " : "  
	                           + ze.getSize() + " bytes");  
	                   long size = ze.getSize();  
	                   if (size > 0) {  
	                       BufferedReader br = new BufferedReader(  
	                               new InputStreamReader(zf.getInputStream(ze)));  
	                       String line;  
	                       while ((line = br.readLine()) != null) {  
	                           System.out.println(line); 
			                   osw = new OutputStreamWriter(new FileOutputStream(src));    
			                   osw.write(line,0,line.length());    
			                   osw.flush(); 
	                       }  
	                       br.close();  
	                   }  
	                   System.out.println();  
	               }  
	           }  
	           zin.closeEntry();  
	       }  
	}
