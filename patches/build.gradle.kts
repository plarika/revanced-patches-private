group = "app.revanced"

patches {
    about {
        name = "FantaMK ReVanced Patches"
        description = "Private maintenance build of ReVanced Patches"
        source = "https://github.com/plarika/revanced-patches-private"
        author = "ReVanced / FantaMK"
        contact = "https://github.com/plarika"
        website = "https://github.com/plarika/revanced-patches-private"
        license = "GNU General Public License v3.0"
    }
}

dependencies {
    // Required due to smali, or build fails. Can be removed once smali is bumped.
    implementation(libs.guava)

    implementation(libs.apksig)

    // Android API stubs defined here.
    compileOnly(project(":patches:stub"))
}

kotlin {
    compilerOptions {
        freeCompilerArgs.addAll(
            "-Xexplicit-backing-fields",
            "-Xcontext-parameters"
        )
    }
}

publishing {
    repositories {
        maven {
            name = "githubPackages"
            url = uri("https://maven.pkg.github.com/plarika/revanced-patches-private")
            credentials(PasswordCredentials::class)
        }
    }
}

apply(from = "strings-processing.gradle.kts")
