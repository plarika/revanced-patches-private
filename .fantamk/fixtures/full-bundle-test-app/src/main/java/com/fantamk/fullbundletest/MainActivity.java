package com.fantamk.fullbundletest;

import android.app.Activity;
import android.graphics.Color;
import android.os.Bundle;
import android.view.Gravity;
import android.widget.LinearLayout;
import android.widget.TextView;

public final class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        LinearLayout root = new LinearLayout(this);
        root.setOrientation(LinearLayout.VERTICAL);
        root.setGravity(Gravity.CENTER);
        root.setPadding(48, 48, 48, 48);
        root.setBackgroundColor(Color.rgb(10, 16, 20));

        TextView title = text("FantaMK Full Bundle Test", 24f, Color.WHITE);
        TextView status = text("Runtime package:\n" + getPackageName(), 20f, Color.rgb(0, 220, 180));
        TextView expected = text("Original: com.fantamk.fullbundletest\nPatched: com.fantamk.fullbundletest.revanced\nVersion: 1.0.0", 14f, Color.LTGRAY);
        root.addView(title); root.addView(status); root.addView(expected); setContentView(root);
    }

    private TextView text(String value, float size, int color) {
        TextView view = new TextView(this); view.setText(value); view.setTextSize(size); view.setTextColor(color); view.setGravity(Gravity.CENTER); view.setPadding(0, 28, 0, 0); return view;
    }
}
