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
 * AndroidManifest.xml权限特征抽取模块，通过解析AndroidManifest.xml文件，
 * 抽取所有uses-permission标记权限，输出到指定格式.output文件中
 * 
 * @author Administrator
 * 
 */
public class ParseAndroidManifest_xml {

	// public static String path="D:\\tao\\test\\apktest\\AndroidManifest.xml";

	public static String appPath = "D:\\tao\\apkSample\\py\\"; // 保存路径

	public static List<String> pathList = new ArrayList<String>(); // AndroidManifest.xml的路径集合

	public static void main(String args[]) {
		try {
			Process pr = Runtime.getRuntime().exec("python " + appPath + "apkParseAndroidManifest_xml.py");
			BufferedReader in = new BufferedReader(new InputStreamReader(pr.getInputStream()));
			String line;
			while ((line = in.readLine()) != null) {
				line = line.replaceAll("/", "\\\\"); // 把路径中的反斜杠"/"替换为"\\"
				pathList.add(line);
			}
			in.close();
			pr.waitFor();
			parsexml(pathList);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	// 解析xml,并将permission属性值输出到permission.csv文件中
	private static void parsexml(List<String> pathList) throws Exception {
		StringBuffer per_str = new StringBuffer(); // 待写入数据
		File file = new File("D:\\tao\\apkSample\\permission.csv"); // 待写入数据的文件
		FileOutputStream out = null;
		if (file.exists()) {
		} else {
			file.createNewFile();// 不存在则创建
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

			// 遍历每一个permission节点
			for (int i = 0; i < permissions.getLength(); i++) {
				Node permission = permissions.item(i);
				// /获取permission节点的所有属性集合
				NamedNodeMap attrs = permission.getAttributes();
				// 遍历permission的属性
				for (int j = 0; j < attrs.getLength(); j++) {
					// 通过item(index)方法获取permission节点的某一个属性
					Node attr = attrs.item(j);
					String permissionVal = attr.getNodeValue().split("\\.")[2];
					// 获取属性名
					// System.out.print("属性名：" + attr.getNodeName());
					// //获取属性值
					// System.out.println("--属性值" + attr.getNodeValue());
					// System.out.println("--属性值" +
					// attr.getNodeValue().substring(18));
					per_str.append("," + permissionVal);
				}
			}
			per_str.append("\r\n"); // 每解析完一个apk，输出换行,注意最后会多出一行，所以循环最后加个trim()除去末尾的换行符
			out.flush();
		}
		out.write(per_str.toString().trim().getBytes("gbk")); // 注意需要转换对应的字符集
		out.close();
		System.out.println("解析成功。。。");
	}

}
