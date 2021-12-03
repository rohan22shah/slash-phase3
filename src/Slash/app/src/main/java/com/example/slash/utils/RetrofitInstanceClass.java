package com.example.slash.utils;
import java.util.concurrent.TimeUnit;

import okhttp3.OkHttpClient;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class RetrofitInstanceClass {

    private static Retrofit retrofit;
    private static OkHttpClient client;

    public static Retrofit getRetrofitInstance() {
        client = new OkHttpClient.Builder().readTimeout(60, TimeUnit.SECONDS)
                .writeTimeout(60, TimeUnit.SECONDS).connectTimeout(60, TimeUnit.SECONDS).build();
        synchronized (RetrofitInstanceClass.class) {
            if (retrofit == null) {
                retrofit = new Retrofit.Builder()
                        .baseUrl("https://slashherokuserver.herokuapp.com")
                        .client(client)
                        .addConverterFactory(GsonConverterFactory.create())
                        .build();
            }
        }
        return retrofit;

    }
}
