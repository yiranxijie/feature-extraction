import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

import org.apache.tools.ant.taskdefs.MacroInstance.Element;
import org.w3c.dom.Document;
import org.w3c.dom.NamedNodeMap;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;


public class ParseAndroidManifest_xml {

	public static String path="D:\\tao\\test\\apktest\\AndroidManifest.xml";
	
	public static void main(String args[]) {
		  Element element = null;
		  File f = new File(path);
		  DocumentBuilder db = null;
		  DocumentBuilderFactory dbf = null;
		  String per_str="";
		  try {
			   dbf = DocumentBuilderFactory.newInstance();
			   db = dbf.newDocumentBuilder();
			   Document document = db.parse(f);
			   NodeList permissions = document.getElementsByTagName("uses-permission");
			   
			 //遍历每一个permission节点
			   for (int i = 0; i < permissions.getLength(); i++) {
				   Node permission = permissions.item(i);
				   //获取permission节点的所有属性集合
				   NamedNodeMap attrs = permission.getAttributes();
				   //遍历permission的属性
				   for (int j = 0; j < attrs.getLength(); j++) {
					   //通过item(index)方法获取permission节点的某一个属性
					   Node attr = attrs.item(j);
					   String permissionVal=attr.getNodeValue().split("\\.")[2];
					   //获取属性名
//					   System.out.print("属性名：" + attr.getNodeName());
//					   //获取属性值
//					   System.out.println("--属性值" + attr.getNodeValue());
//					   System.out.println("--属性值" + attr.getNodeValue().substring(18));
					   per_str+=permissionVal+ ".";
				   }
			  }
			   System.out.println(per_str);
			   writeToOutput(per_str);
		  }catch (Exception e) {
		   e.printStackTrace();
		 }
		}

	//将permission属性值输出到permission.output文件中
	private static void writeToOutput(String permissionStr) {
		String str = new String(); //原有txt内容  
        String s1 = new String();//内容更新
		try {  
            File f = new File("D:\\tao\\test\\apktest\\permission.output");  
            if (f.exists()) {  
                System.out.println("文件存在");  
            } else {  
                System.out.println("文件不存在");  
                f.createNewFile();// 不存在则创建  
            }  
            BufferedReader input = new BufferedReader(new FileReader(f));  
  
            while ((str = input.readLine()) != null) {  
                s1 += str;  
            }  
            System.out.println(s1);  
            input.close();  
            s1 += permissionStr;  
            String []strs=s1.split("\\.");
  
            BufferedWriter output = new BufferedWriter(new FileWriter(f));  
            output.write(s1);  
            output.close();  
        } catch (Exception e) {  
            e.printStackTrace();  
  
        } 
	}
}
