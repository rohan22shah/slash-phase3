package com.example.slash.utils;

import com.example.slash.entities.SearchResultEntity;

import java.util.ArrayList;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Path;

public interface ApiInterface {

    @GET("/{site}/{product}")
    Call<ArrayList<SearchResultEntity>> getAllResults(@Path("site") String site,@Path("product") String product);



}
