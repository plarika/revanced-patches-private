plugins {
    id("com.android.application") version "9.0.1"
}

android {
    namespace = "com.fantamk.fullbundletest"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.fantamk.fullbundletest"
        minSdk = 26
        targetSdk = 34
        versionCode = 1
        versionName = "1.0.0"
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
}
