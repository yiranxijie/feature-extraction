import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

import org.apache.tools.ant.types.CommandlineJava.SysProperties;

/**
 * apk预处理模块，通过apktool工具解压.apk文件得到相应的文件
 * 
 * @author tao
 * 
 */
public class APK_Pretreatment {

	public static String path = "C:\\Windows"; // apktool路径

	public static String appPath = "D:\\tao\\apkSample\\py\\"; // 保存路径

	public static void main(String args[]) throws IOException {
		
	}

	//java运行python脚本解压apk
	public void decompress() {
		Process process = null;
		try {

			File file = new File(path);

			process = Runtime.getRuntime().exec("python " + appPath + "apkPretreatment.py");
			if (process.waitFor() != 0) {
				System.out.println("解压失败。。。");
			}else{
				System.out.println("解压完成。。。");
			}

		} catch (Exception e) {
			e.printStackTrace();
		}
	}

}