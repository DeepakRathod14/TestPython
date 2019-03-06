package selenium;

import java.io.File;
import java.io.IOException;
import java.time.Duration;
import java.util.Set;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.CacheLookup;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.How;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.FluentWait;
import org.openqa.selenium.support.ui.Wait;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.annotations.Test;

//@Listeners(selenium.TestListener.class)
public class WaitClass {
	
	@FindBy(how=How.ID, using="")
	@CacheLookup
	private WebElement ele;
	
	@FindBy(id="")
	private WebElement eleID;
	
	static WebDriver driver;
	static WebDriverWait wait;
	
	
	@Test(priority=1)
	public void scenario01() throws IOException
	{
		System.out.println(Thread.activeCount());
		File driverPath = new File("/home/deepak/Installer Files/chromedriver").getCanonicalFile();
		System.setProperty("webdriver.chrome.driver", driverPath.getCanonicalPath());
		
		driver = new ChromeDriver();
		driver.get("http://www.google.com");
		driver.manage().logs().get("driver");
		driver.manage().window().maximize();
		Set<String> logs = driver.manage().logs().getAvailableLogTypes();
		logs.forEach(log -> System.out.println(log));
		wait = new WebDriverWait(driver, 8);
	}
	
	
	@Test(priority=2)
	public void down()
	{
		driver.quit();
	}
	@Test(enabled=false)
	public void scenario02()
	{
		//Implicit wait
		driver.manage().timeouts().implicitlyWait(300, TimeUnit.MILLISECONDS);
		//Explicit wait
		wait=new WebDriverWait(driver, 10);
		WebElement ele = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("")));
		//Fluent Wait
		Wait wait = new FluentWait<>(driver)
				.ignoring(NoSuchElementException.class, Exception.class)
				.withTimeout(Duration.ofSeconds(10, 10))
				.pollingEvery(Duration.ofMillis(500));
		
//		wait.until()
		
		
	}
	
}
