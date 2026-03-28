# -------- Stage 1: Build --------
FROM maven:3.9.9-eclipse-temurin-17 AS builder

WORKDIR /build

# Copy pom.xml first (cache dependencies)
COPY pom.xml .
RUN mvn dependency:go-offline

# Copy source code
COPY src ./src

# Build JAR
RUN mvn clean package -DskipTests


# -------- Stage 2: Run --------
FROM eclipse-temurin:17-jdk-alpine

WORKDIR /app

# Copy JAR from builder
COPY --from=builder /build/target/*.jar app.jar

# Expose port
EXPOSE 8080

# Run app
ENTRYPOINT ["java", "-jar", "app.jar"]