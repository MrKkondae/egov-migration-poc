<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<groupId>kr.co.openpaas</groupId>
	<artifactId>hello-egov-board</artifactId>
	<packaging>war</packaging>
	<version>1.0.0</version>
	<name>hello-egov-board</name>
	<url>http://www.egovframe.go.kr</url>

	<properties>
		<maven.compiler.source>17</maven.compiler.source>
		<maven.compiler.target>17</maven.compiler.target>
		<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
		<spring.maven.artifact.version>3.5.x</spring.maven.artifact.version>
		<egovframework.rte.version>4.3.0</egovframework.rte.version>
	</properties>

	<repositories>
		<repository>
			<id>mvn2</id>
			<url>https://repo1.maven.org/maven2/</url>
		</repository>
		<repository>
			<id>egovframe</id>
			<url>https://maven.egovframe.go.kr/maven/</url>
		</repository>
	</repositories>

	<dependencies>
        <!-- 표준프레임워크 실행환경 -->
        <dependency>
            <groupId>org.egovframe.rte</groupId>
            <artifactId>egovframework.rte.ptl.mvc</artifactId>
            <version>${egovframework.rte.version}</version>
            <exclusions>
                <exclusion>
                    <artifactId>commons-logging</artifactId>
                    <groupId>commons-logging</groupId>
                </exclusion>
            </exclusions>
        </dependency>
        <dependency>
            <groupId>org.egovframe.rte</groupId>
            <artifactId>egovframework.rte.psl.dataaccess</artifactId>
            <version>${egovframework.rte.version}</version>
        </dependency>
        <dependency>
            <groupId>org.egovframe.rte</groupId>
            <artifactId>egovframework.rte.fdl.idgnr</artifactId>
            <version>${egovframework.rte.version}</version>
        </dependency>
        <dependency>
            <groupId>org.egovframe.rte</groupId>
            <artifactId>egovframework.rte.fdl.property</artifactId>
            <version>${egovframework.rte.version}</version>
        </dependency>

        <!-- Spring Boot dependencies -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-security</artifactId>
        </dependency>

        <!-- Database dependencies -->
        <dependency>
            <groupId>com.h2database</groupId>
            <artifactId>h2</artifactId>
            <scope>runtime</scope>
        </dependency>

        <!-- Other dependencies -->
        <dependency>
            <groupId>org.apache.commons</groupId>
            <artifactId>commons-collections4</artifactId>
        </dependency>
        <dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-databind</artifactId>
        </dependency>

		<dependency>
            <groupId>org.antlr</groupId>
            <artifactId>antlr</artifactId>
            <version>3.5</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
		<dependency>
			<groupId>egovframework.rte</groupId>
			<artifactId>egovframework.rte.fdl.security</artifactId>
			<version>${egovframework.rte.version}</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
		<dependency>
            <groupId>egovframework.rte</groupId>
            <artifactId>egovframework.rte.fdl.excel</artifactId>
            <version>${egovframework.rte.version}</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>com.googlecode.log4jdbc</groupId>
            <artifactId>log4jdbc</artifactId>
            <version>1.2</version>
            <exclusions>
                <exclusion>
                    <artifactId>slf4j-api</artifactId>
                    <groupId>org.slf4j</groupId>
                </exclusion>
            </exclusions>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>org.jasypt</groupId>
            <artifactId>jasypt</artifactId>
            <version>1.9.2</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>cglib</groupId>
            <artifactId>cglib</artifactId>
            <version>3.1</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>org.apache.commons</groupId>
            <artifactId>commons-compress</artifactId>
            <version>1.8.1</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>xerces</groupId>
            <artifactId>xercesImpl</artifactId>
            <version>2.11.0</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>net.sf.ehcache</groupId>
            <artifactId>ehcache-core</artifactId>
            <version>2.6.9</version>
            <exclusions>
                <exclusion>
                    <artifactId>slf4j-api</artifactId>
                    <groupId>org.slf4j</groupId>
                </exclusion>
            </exclusions>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
		<dependency>
            <groupId>org.quartz-scheduler</groupId>
            <artifactId>quartz</artifactId>
            <version>2.1.7</version>
            <exclusions>
                <exclusion>
                    <artifactId>slf4j-api</artifactId>
                    <groupId>org.slf4j</groupId>
                </exclusion>
            </exclusions>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>org.quartz-scheduler</groupId>
            <artifactId>quartz-jobs</artifactId>
            <version>2.2.1</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>oro</groupId>
            <artifactId>oro</artifactId>
            <version>2.0.8</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>com.ibm.icu</groupId>
            <artifactId>icu4j</artifactId>
            <version>53.1</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>commons-net</groupId>
            <artifactId>commons-net</artifactId>
            <version>3.3</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>org.apache.commons</groupId>
            <artifactId>commons-email</artifactId>
            <version>1.3.2</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>egovframework.com.ems</groupId>
            <artifactId>sndng-mail</artifactId>
            <version>1.0</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>javax.servlet.jsp</groupId>
            <artifactId>javax.servlet.jsp-api</artifactId>
            <version>2.3.1</version>
            <scope>provided</scope>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>ldapsdk</groupId>
            <artifactId>ldapsdk</artifactId>
            <version>4.1</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>com.artofsolving</groupId>
            <artifactId>jodconverter</artifactId>
            <version>2.2.1</version>
            <exclusions>
                <exclusion>
                    <artifactId>slf4j-api</artifactId>
                    <groupId>org.slf4j</groupId>
                </exclusion>
                <exclusion>
                    <artifactId>commons-io</artifactId>
                    <groupId>commons-io</groupId>
                </exclusion>
            </exclusions>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>xmlbeans</groupId>
            <artifactId>xbean</artifactId>
            <version>2.2.0</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>commons-fileupload</groupId>
            <artifactId>commons-fileupload</artifactId>
            <version>1.3.1</version>
            <exclusions>
                <exclusion>
                    <artifactId>commons-io</artifactId>
                    <groupId>commons-io</groupId>
                </exclusion>
            </exclusions>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>org.twitter4j</groupId>
            <artifactId>twitter4j-core</artifactId>
            <version>4.0.2</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>net.sourceforge.ajaxtags</groupId>
            <artifactId>ajaxtags</artifactId>
            <version>1.5.7</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>net.sourceforge.ajaxtags</groupId>
            <artifactId>ajaxtags-resources</artifactId>
            <version>1.5.7</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>com.ckeditor</groupId>
            <artifactId>ckeditor-java-core</artifactId>
            <version>3.5.3</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>org.apache.xmlgraphics</groupId>
            <artifactId>batik-ext</artifactId>
            <version>1.7</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>5.1.31</version>
        </dependency>

		<dependency>
			<groupId>javax.annotation</groupId>
			<artifactId>javax.annotation-api</artifactId>
			<version>1.3.2</version>
		</dependency>
	</dependencies>

	<build>
        <defaultGoal>install</defaultGoal>
        <directory>${basedir}/target</directory>
        <finalName>${artifactId}-${version}</finalName>
        <pluginManagement>
            <plugins>
                <plugin>
	                <groupId>org.apache.tomcat.maven</groupId>
	                <artifactId>tomcat7-maven-plugin</artifactId>
	                <version>2.2</version>
	                <configuration>
	                    <port>80</port>
	                    <path>/</path>
	                    <systemProperties>
	                        <JAVA_OPTS>-Xms256m -Xmx768m -XX:MaxPermSize=256m</JAVA_OPTS>
	                    </systemProperties>
	                </configuration>
	            </plugin>
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-compiler-plugin</artifactId>
                    <configuration>
                        <source>17</source>
                        <target>17</target>
                        <encoding>UTF-8</encoding>
                    </configuration>
                </plugin>
            </plugins>
        </pluginManagement>
        <plugins>
            <!-- JavaDoc -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-javadoc-plugin</artifactId>
                <version>3.2.0</version>
            </plugin>
        </plugins>
    </build>
    <reporting>
        <outputDirectory>${basedir}/target/site</outputDirectory>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-project-info-reports-plugin</artifactId>
                <version>3.1.2</version>
                <reportSets>
                    <reportSet>
                        <id>sunlink</id>
                        <reports>
                            <report>javadoc</report>
                        </reports>
                        <inherited>true</inherited>
                        <configuration>
                            <links>
                                <link>http://docs.oracle.com/javase/17/docs/api/</link>
                            </links>
                        </configuration>
                    </reportSet>
                </reportSets>
            </plugin>
        </plugins>
    </reporting>
</project>




```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<groupId>kr.co.openpaas</groupId>
	<artifactId>hello-egov-board</artifactId>
	<packaging>war</packaging>
	<version>1.0.0</version>
	<name>hello-egov-board</name>
	<url>http://www.egovframe.go.kr</url>

	<properties>
		<maven.compiler.source>17</maven.compiler.source>
		<maven.compiler.target>17</maven.compiler.target>
		<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
		<spring.maven.artifact.version>3.5.x</spring.maven.artifact.version>
		<egovframework.rte.version>4.3.0</egovframework.rte.version>
	</properties>

	<repositories>
		<repository>
			<id>mvn2</id>
			<url>https://repo1.maven.org/maven2/</url>
		</repository>
		<repository>
			<id>egovframe</id>
			<url>https://maven.egovframe.go.kr/maven/</url>
		</repository>
	</repositories>

	<dependencies>
        <!-- 표준프레임워크 실행환경 -->
        <dependency>
            <groupId>org.egovframe.rte</groupId>
            <artifactId>egovframework.rte.ptl.mvc</artifactId>
            <version>${egovframework.rte.version}</version>
            <exclusions>
                <exclusion>
                    <artifactId>commons-logging</artifactId>
                    <groupId>commons-logging</groupId>
                </exclusion>
            </exclusions>
        </dependency>
        <dependency>
            <groupId>org.egovframe.rte</groupId>
            <artifactId>egovframework.rte.psl.dataaccess</artifactId>
            <version>${egovframework.rte.version}</version>
        </dependency>
        <dependency>
            <groupId>org.egovframe.rte</groupId>
            <artifactId>egovframework.rte.fdl.idgnr</artifactId>
            <version>${egovframework.rte.version}</version>
        </dependency>
        <dependency>
            <groupId>org.egovframe.rte</groupId>
            <artifactId>egovframework.rte.fdl.property</artifactId>
            <version>${egovframework.rte.version}</version>
        </dependency>

        <!-- Spring Boot dependencies -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-security</artifactId>
        </dependency>

        <!-- Database dependencies -->
        <dependency>
            <groupId>com.h2database</groupId>
            <artifactId>h2</artifactId>
            <scope>runtime</scope>
        </dependency>

        <!-- Other dependencies -->
        <dependency>
            <groupId>org.apache.commons</groupId>
            <artifactId>commons-collections4</artifactId>
        </dependency>
        <dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-databind</artifactId>
        </dependency>

		<dependency>
            <groupId>org.antlr</groupId>
            <artifactId>antlr</artifactId>
            <version>3.5</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
		<dependency>
			<groupId>egovframework.rte</groupId>
			<artifactId>egovframework.rte.fdl.security</artifactId>
			<version>${egovframework.rte.version}</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
		<dependency>
            <groupId>egovframework.rte</groupId>
            <artifactId>egovframework.rte.fdl.excel</artifactId>
            <version>${egovframework.rte.version}</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>com.googlecode.log4jdbc</groupId>
            <artifactId>log4jdbc</artifactId>
            <version>1.2</version>
            <exclusions>
                <exclusion>
                    <artifactId>slf4j-api</artifactId>
                    <groupId>org.slf4j</groupId>
                </exclusion>
            </exclusions>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>org.jasypt</groupId>
            <artifactId>jasypt</artifactId>
            <version>1.9.2</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>cglib</groupId>
            <artifactId>cglib</artifactId>
            <version>3.1</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>org.apache.commons</groupId>
            <artifactId>commons-compress</artifactId>
            <version>1.8.1</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>xerces</groupId>
            <artifactId>xercesImpl</artifactId>
            <version>2.11.0</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>net.sf.ehcache</groupId>
            <artifactId>ehcache-core</artifactId>
            <version>2.6.9</version>
            <exclusions>
                <exclusion>
                    <artifactId>slf4j-api</artifactId>
                    <groupId>org.slf4j</groupId>
                </exclusion>
            </exclusions>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
		<dependency>
            <groupId>org.quartz-scheduler</groupId>
            <artifactId>quartz</artifactId>
            <version>2.1.7</version>
            <exclusions>
                <exclusion>
                    <artifactId>slf4j-api</artifactId>
                    <groupId>org.slf4j</groupId>
                </exclusion>
            </exclusions>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>org.quartz-scheduler</groupId>
            <artifactId>quartz-jobs</artifactId>
            <version>2.2.1</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>oro</groupId>
            <artifactId>oro</artifactId>
            <version>2.0.8</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>com.ibm.icu</groupId>
            <artifactId>icu4j</artifactId>
            <version>53.1</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>commons-net</groupId>
            <artifactId>commons-net</artifactId>
            <version>3.3</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>org.apache.commons</groupId>
            <artifactId>commons-email</artifactId>
            <version>1.3.2</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>egovframework.com.ems</groupId>
            <artifactId>sndng-mail</artifactId>
            <version>1.0</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>javax.servlet.jsp</groupId>
            <artifactId>javax.servlet.jsp-api</artifactId>
            <version>2.3.1</version>
            <scope>provided</scope>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>ldapsdk</groupId>
            <artifactId>ldapsdk</artifactId>
            <version>4.1</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>com.artofsolving</groupId>
            <artifactId>jodconverter</artifactId>
            <version>2.2.1</version>
            <exclusions>
                <exclusion>
                    <artifactId>slf4j-api</artifactId>
                    <groupId>org.slf4j</groupId>
                </exclusion>
                <exclusion>
                    <artifactId>commons-io</artifactId>
                    <groupId>commons-io</groupId>
                </exclusion>
            </exclusions>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>xmlbeans</groupId>
            <artifactId>xbean</artifactId>
            <version>2.2.0</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>commons-fileupload</groupId>
            <artifactId>commons-fileupload</artifactId>
            <version>1.3.1</version>
            <exclusions>
                <exclusion>
                    <artifactId>commons-io</artifactId>
                    <groupId>commons-io</groupId>
                </exclusion>
            </exclusions>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>org.twitter4j</groupId>
            <artifactId>twitter4j-core</artifactId>
            <version>4.0.2</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>net.sourceforge.ajaxtags</groupId>
            <artifactId>ajaxtags</artifactId>
            <version>1.5.7</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>net.sourceforge.ajaxtags</groupId>
            <artifactId>ajaxtags-resources</artifactId>
            <version>1.5.7</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>com.ckeditor</groupId>
            <artifactId>ckeditor-java-core</artifactId>
            <version>3.5.3</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>org.apache.xmlgraphics</groupId>
            <artifactId>batik-ext</artifactId>
            <version>1.7</version>
        </dependency>

		<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>5.1.31</version>
        </dependency>

		<dependency>
			<groupId>javax.annotation</groupId>
			<artifactId>javax.annotation-api</artifactId>
			<version>1.3.2</version>
		</dependency>
	</dependencies>

	<build>
        <defaultGoal>install</defaultGoal>
        <directory>${basedir}/target</directory>
        <finalName>${artifactId}-${version}</finalName>
        <pluginManagement>
            <plugins>
                <plugin>
	                <groupId>org.apache.tomcat.maven</groupId>
	                <artifactId>tomcat7-maven-plugin</artifactId>
	                <version>2.2</version>
	                <configuration>
	                    <port>80</port>
	                    <path>/</path>
	                    <systemProperties>
	                        <JAVA_OPTS>-Xms256m -Xmx768m -XX:MaxPermSize=256m</JAVA_OPTS>
	                    </systemProperties>
	                </configuration>
	            </plugin>
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-compiler-plugin</artifactId>
                    <configuration>
                        <source>17</source>
                        <target>17</target>
                        <encoding>UTF-8</encoding>
                    </configuration>
                </plugin>
            </plugins>
        </pluginManagement>
        <plugins>
            <!-- JavaDoc -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-javadoc-plugin</artifactId>
                <version>3.2.0</version>
            </plugin>
        </plugins>
    </build>
    <reporting>
        <outputDirectory>${basedir}/target/site</outputDirectory>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-project-info-reports-plugin</artifactId>
                <version>3.1.2</version>
                <reportSets>
                    <reportSet>
                        <id>sunlink</id>
                        <reports>
                            <report>javadoc</report>
                        </reports>
                        <inherited>true</inherited>
                        <configuration>
                            <links>
                                <link>http://docs.oracle.com/javase/17/docs/api/</link>
                            </links>
                        </configuration>
                    </reportSet>
                </reportSets>
            </plugin>
        </plugins>
    </reporting>
</project>
```

### 확정 변환된 eGov dependency 목록
- org.egovframe.rte:egovframework.rte.ptl.mvc
- org.egovframe.rte:egovframework.rte.psl.dataaccess
- org.egovframe.rte:egovframework.rte.fdl.idgnr
- org.egovframe.rte:egovframework.rte.fdl.property

### 좌표 확인이 필요하여 `TODO`로 남긴 항목 목록
- org.egovframe.rte:egovframework.rte.fdl.security
- org.egovframe.rte:egovframework.rte.fdl.excel
- com.googlecode.log4jdbc:log4jdbc
- org.jasypt:jasypt
- cglib:cglib
- org.apache.commons:commons-compress
- xerces:xercesImpl
- net.sf.ehcache:ehcache-core
- org.quartz-scheduler:quartz
- org.quartz-scheduler:quartz-jobs
- oro:oro
- com.ibm.icu:icu4j
- commons-net:commons-net
- org.apache.commons:commons-email
- egovframework.com.ems:sndng-mail
- javax.servlet.jsp:javax.servlet.jsp-api
- ldapsdk:ldapsdk
- com.artofsolving:jodconverter
- xmlbeans:xbean
- commons-fileupload:commons-fileupload
- org.twitter4j:twitter4j-core
- net.sourceforge.ajaxtags:ajaxtags
- net.sourceforge.ajaxtags:ajaxtags-resources
- com.ckeditor:ckeditor-java-core
- org.apache.xmlgraphics:batik-ext

### 수동 검토 필요 항목
- MyBatis 전환 필요
- Jakarta 기반의 javax.servlet 계열의 대체 확인