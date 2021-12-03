package com.example.slash;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.example.slash.adapters.SearchResultsListAdapter;
import com.example.slash.entities.SearchResultEntity;

import java.util.ArrayList;

public class SearchResultActivity extends AppCompatActivity {

    Activity activity;
    RecyclerView rvSearchResult;
    SearchResultsListAdapter adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_search_result);
        activity = this;
        Intent intent = activity.getIntent();
        Bundle args = intent.getBundleExtra("bundle");
        ArrayList<SearchResultEntity> list;
        list = (ArrayList<SearchResultEntity>) args.getSerializable("result-array");
        rvSearchResult =findViewById(R.id.rvSearchResult);
        adapter = new SearchResultsListAdapter(activity, list);
        LinearLayoutManager linearLayoutManager =new LinearLayoutManager(activity);
        rvSearchResult.setLayoutManager(linearLayoutManager);
        rvSearchResult.setAdapter(adapter);
    }
}