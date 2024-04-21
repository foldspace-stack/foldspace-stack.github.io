import java.lang.reflect.Proxy;
import java.util.Map;

public class DyProxy {
    static private Map proxyInstance = (Map) Proxy.newProxyInstance(
            DyProxy.class.getClassLoader(), 
            new Class[] { Map.class }, 
            (proxy, method, methodArgs) -> {
                if (method.getName().equals("get")) {
                    return 42;
                } else {
                    throw new UnsupportedOperationException(
                            "Unsupported method: " + method.getName());
                }
            });
    public static void main(String[] args){
        proxyInstance.get("hello"); // 42
        
    }
}