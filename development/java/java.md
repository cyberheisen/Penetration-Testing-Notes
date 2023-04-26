# java

## compiling java code

```
javac -source <version> -target <version> <java file> // compiles a java file 
echo "Main-Class: test" > META-INF/MANIFEST.MF // is required 
jar cmf META-INF/MANIFEST.MF <jar file> <class file> 
```

## executing java jar files
```
java -jar <jar file>
```

## basic java program
```
public class HelloWorld {

    public static void main(String[] args) {
        System.out.println("Hello World!");
    }

}
```

## reading and writing files
```
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class FileReadWrite {

    public static void main(String[] args) {
        String inputFile = "input.txt";
        String outputFile = "output.txt";

        // Read from file
        String fileContents = readFile(inputFile);
        System.out.println("Contents of " + inputFile + ":");
        System.out.println(fileContents);

        // Write to file
        String outputString = "This is some text to write to the output file.";
        writeFile(outputFile, outputString);
        System.out.println("Wrote the following to " + outputFile + ":");
        System.out.println(outputString);
    }

    public static String readFile(String filePath) {
        StringBuilder sb = new StringBuilder();

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                sb.append(line).append("\n");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        return sb.toString();
    }

    public static void writeFile(String filePath, String outputString) {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(filePath))) {
            bw.write(outputString);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

## Web Requests

```
import java.net.HttpURLConnection;
import java.net.URL;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.IOException;

public class HttpFunctions {

    public static void main(String[] args) {
        try {
            // Make a GET request
            String getUrl = "http://example.com/";
            String getResponse = httpGet(getUrl);
            System.out.println("GET response: " + getResponse);

            // Make a POST request
            String postUrl = "http://example.com/post";
            String postPayload = "key1=value1&key2=value2";
            String postResponse = httpPost(postUrl, postPayload);
            System.out.println("POST response: " + postResponse);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static String httpGet(String urlStr) throws IOException {
        URL url = new URL(urlStr);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("GET");

        BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        String inputLine;
        StringBuilder response = new StringBuilder();
        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();

        return response.toString();
    }

    public static String httpPost(String urlStr, String payload) throws IOException {
        URL url = new URL(urlStr);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("POST");
        conn.setDoOutput(true);

        OutputStream os = conn.getOutputStream();
        os.write(payload.getBytes());
        os.flush();
        os.close();

        BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        String inputLine;
        StringBuilder response = new StringBuilder();
        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();

        return response.toString();
    }
}
```
