import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class TestThreadPool {
    public static void main(String[] args) throws InterruptedException {
    ExecutorService threadPool = Executors.newFixedThreadPool(10);
    while(true) {
        threadPool.execute(new Runnable() { // 提交多个线程任务，并执行
            private Long liveTime;
            @Override
            public void run(){
                System.out.println("ThreadName:"+Thread.currentThread().getName() +" threadId:"+Thread.currentThread().getId()+ " is running ..");
                try {
                    Thread.sleep(3000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });
        System.out.println("thread add"+threadPool.toString());
        Thread.sleep(100*2);
    }
    }
}
