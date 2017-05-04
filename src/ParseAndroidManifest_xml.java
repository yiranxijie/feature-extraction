import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.List;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

import org.apache.tools.ant.taskdefs.MacroInstance.Element;
import org.w3c.dom.Document;
import org.w3c.dom.NamedNodeMap;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

/**
 * AndroidManifest.xmlȨ��������ȡģ�飬ͨ������AndroidManifest.xml�ļ���
 * ��ȡ����uses-permission���Ȩ�ޣ������ָ����ʽ.output�ļ���
 * 
 * @author Administrator
 * 
 */
public class ParseAndroidManifest_xml {

	// public static String path="D:\\tao\\test\\apktest\\AndroidManifest.xml";

	public static String appPath = "D:\\tao\\apkSample\\py\\"; // ����·��

	public static List<String> pathList = new ArrayList<String>(); // AndroidManifest.xml��·������

	public static void main(String args[]) {
		try {
			Process pr = Runtime.getRuntime().exec("python " + appPath + "apkParseAndroidManifest_xml.py");
			BufferedReader in = new BufferedReader(new InputStreamReader(pr.getInputStream()));
			String line;
			while ((line = in.readLine()) != null) {
				line = line.replaceAll("/", "\\\\"); // ��·���еķ�б��"/"�滻Ϊ"\\"
				pathList.add(line);
			}
			in.close();
			pr.waitFor();
			parsexml(pathList);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	// ����xml,����permission����ֵ�����permission.csv�ļ���
	private static void parsexml(List<String> pathList) throws Exception {
		StringBuffer per_str = new StringBuffer(); // ��д������
		File file = new File("D:\\tao\\apkSample\\permission.csv"); // ��д�����ݵ��ļ�
		FileOutputStream out = null;
		if (file.exists()) {
		} else {
			file.createNewFile();// �������򴴽�
		}

		out = new FileOutputStream(file, false);

		for (String path : pathList) {
			Element element = null;
			File f = new File(path);
			DocumentBuilder db = null;
			DocumentBuilderFactory dbf = null;
			String appname = path.split("\\\\")[2];
			per_str.append(appname + ".apk");

			dbf = DocumentBuilderFactory.newInstance();
			db = dbf.newDocumentBuilder();
			Document document = db.parse(f);
			NodeList permissions = document.getElementsByTagName("uses-permission");

			// ����ÿһ��permission�ڵ�
			for (int i = 0; i < permissions.getLength(); i++) {
				Node permission = permissions.item(i);
				// /��ȡpermission�ڵ���������Լ���
				NamedNodeMap attrs = permission.getAttributes();
				// ����permission������
				for (int j = 0; j < attrs.getLength(); j++) {
					// ͨ��item(index)������ȡpermission�ڵ��ĳһ������
					Node attr = attrs.item(j);
					String permissionVal = attr.getNodeValue().split("\\.")[2];
					// ��ȡ������
					// System.out.print("��������" + attr.getNodeName());
					// //��ȡ����ֵ
					// System.out.println("--����ֵ" + attr.getNodeValue());
					// System.out.println("--����ֵ" +
					// attr.getNodeValue().substring(18));
					per_str.append("," + permissionVal);
				}
			}
			per_str.append("\r\n"); // ÿ������һ��apk���������,ע��������һ�У�����ѭ�����Ӹ�trim()��ȥĩβ�Ļ��з�
			out.flush();
		}
		out.write(per_str.toString().trim().getBytes("gbk")); // ע����Ҫת����Ӧ���ַ���
		out.close();
		System.out.println("�����ɹ�������");
	}

}
