package com.example.slash;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.Spinner;

import androidx.appcompat.app.AppCompatActivity;

import com.example.slash.entities.SearchResultEntity;
import com.example.slash.utils.ApiInterface;
import com.example.slash.utils.RetrofitInstanceClass;
import com.google.android.material.textfield.TextInputEditText;
import com.google.android.material.textfield.TextInputLayout;

import java.io.Serializable;
import java.util.ArrayList;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class MainActivity extends AppCompatActivity {

    Activity activity;
    TextInputLayout tilSearch;
    TextInputEditText etSearch;
    Button btnSearch;
    Spinner spinnerSite;
    String site;

    private void findViews() {
        tilSearch = findViewById(R.id.tilSearch);
        etSearch = findViewById(R.id.etSearch);
        btnSearch = findViewById(R.id.btnSearch);
        spinnerSite = findViewById(R.id.spinnerSite);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        activity = this;
        findViews();
        ArrayAdapter<CharSequence> arrayAdapter = ArrayAdapter.createFromResource(this, R.array.spinner_list, android.R.layout.simple_spinner_item);
        arrayAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinnerSite.setAdapter(arrayAdapter);
        spinnerSite.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> adapterView, View view, int pos, long l) {
                site = adapterView.getItemAtPosition(pos).toString();
                Log.d("site-name", site);
            }

            @Override
            public void onNothingSelected(AdapterView<?> adapterView) {

            }
        });


    }

    public void search(View view) {
        String product = tilSearch.getEditText().getText().toString();
        getSearchResults(site, product);

    }

    public void getSearchResults(String site, String product) {
        ApiInterface apiInterface = RetrofitInstanceClass.getRetrofitInstance().create(ApiInterface.class);
        Log.d("site-product", site + " & " + product);
        if (site.equals("Walmart")) {
            site = "wm";
        } else if (site.equals("Amazon")) {
            site = "az";
        } else if (site.equals("Ebay")) {
            site = "eb";
        } else if (site.equals("CostCo")) {
            site = "cc";
        } else if (site.equals("All")) {
            site = "all";
        } else if (site.equals("Target")) {
            site = "tg";
        } else if (site.equals("BestBuy")) {
            site = "bb";
        }
        Log.d("site-product", site + " & " + product);
        Call<ArrayList<SearchResultEntity>> call = apiInterface.getAllResults(site, product);
        call.enqueue(new Callback<ArrayList<SearchResultEntity>>() {
            @Override
            public void onResponse(Call<ArrayList<SearchResultEntity>> call, Response<ArrayList<SearchResultEntity>> response) {
                ArrayList<SearchResultEntity> list = response.body();
                Intent intent = new Intent(activity, SearchResultActivity.class);
                Bundle bundle = new Bundle();
                bundle.putSerializable("result-array", (Serializable) list);
                intent.putExtra("bundle", bundle);
                startActivity(intent);
                finish();
            }

            @Override
            public void onFailure(Call<ArrayList<SearchResultEntity>> call, Throwable t) {

            }
        });
    }

    @Override
    public void onBackPressed() {
        super.onBackPressed();
    }
}