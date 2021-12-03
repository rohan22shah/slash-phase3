package com.example.slash;

import android.app.Activity;
import android.content.Intent;
import android.os.Handler;
import android.view.Window;
import android.view.WindowManager;
import android.widget.ImageView;

import androidx.appcompat.app.AppCompatActivity;

public class SplashActivity extends AppCompatActivity {

    Window window;
    ImageView iv_Logo;
    android.widget.TextView application_Name;
    Activity activity;

    @Override
    protected void onCreate(android.os.Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_splash_screen);

        activity = this;
        iv_Logo = findViewById(R.id.iv_Logo);
        application_Name = findViewById(R.id.application_Name);

        window = getWindow();
        window.setFlags(WindowManager.LayoutParams.FLAG_LAYOUT_NO_LIMITS,
                WindowManager.LayoutParams.FLAG_LAYOUT_NO_LIMITS);
        redirectToMain();

    }

    void redirectToMain() {

        new Handler().postDelayed(new Runnable() {

            public void run() {
                Intent intent = new Intent(activity, MainActivity.class);
                startActivity(intent);
                finish();
            }
        }, 1800);

    }



}
