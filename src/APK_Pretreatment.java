import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

import org.apache.tools.ant.types.CommandlineJava.SysProperties;

/**
 * apkԤ����ģ�飬ͨ��apktool���߽�ѹ.apk�ļ��õ���Ӧ���ļ�
 * 
 * @author tao
 * 
 */
public class APK_Pretreatment {

	public static String path = "C:\\Windows"; // apktool·��

	public static String appPath = "D:\\tao\\apkSample\\py\\"; // ����·��

	public static void main(String args[]) throws IOException {
		
	}

	//java����python�ű���ѹapk
	public void decompress() {
		Process process = null;
		try {

			File file = new File(path);

			process = Runtime.getRuntime().exec("python " + appPath + "apkPretreatment.py");
			if (process.waitFor() != 0) {
				System.out.println("��ѹʧ�ܡ�����");
			}else{
				System.out.println("��ѹ��ɡ�����");
			}

		} catch (Exception e) {
			e.printStackTrace();
		}
	}

}