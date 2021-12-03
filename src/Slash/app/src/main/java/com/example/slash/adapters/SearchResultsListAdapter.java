package com.example.slash.adapters;

import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.cardview.widget.CardView;
import androidx.recyclerview.widget.RecyclerView;

import com.example.slash.R;
import com.example.slash.entities.SearchResultEntity;

import java.util.ArrayList;

public class SearchResultsListAdapter extends RecyclerView.Adapter<SearchResultsListAdapter.SearchResultsViewHolder> {

    Activity activity;
    ArrayList<SearchResultEntity> list;

    public SearchResultsListAdapter(Activity activity, ArrayList<SearchResultEntity> list){
        this.activity=activity;
        this.list = list;
    }

    @NonNull
    @Override
    public SearchResultsViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View itemView = LayoutInflater.from(parent.getContext()).inflate(R.layout.layout_search_result_card, parent, false);
        return new SearchResultsListAdapter.SearchResultsViewHolder(itemView);
    }

    @Override
    public void onBindViewHolder(@NonNull SearchResultsViewHolder holder, int position) {
        holder.tvItemTitle.setText(list.get(position).getTitle());
        holder.tvItemPrice.setText(list.get(position).getPrice());
        holder.tvItemLink.setText(list.get(position).getLink());
        if (list.get(position).getWebsite().equals("amazon")){
            holder.ivWebsiteLogo.setImageResource(R.drawable.amazon_logo);
        }else if (list.get(position).getWebsite().equals("target")){
            holder.ivWebsiteLogo.setImageResource(R.drawable.target_logo);
        }else if (list.get(position).getWebsite().equals("walmart")){
            holder.ivWebsiteLogo.setImageResource(R.drawable.walmart_logo);
        }else if (list.get(position).getWebsite().equals("ebay")){
            holder.ivWebsiteLogo.setImageResource(R.drawable.ebay_logo);
        }
    }

    @Override
    public int getItemCount() {
        return this.list.size();
    }

    public class SearchResultsViewHolder extends RecyclerView.ViewHolder{

        CardView cvSearchResult;
        TextView tvItemPrice;
        TextView tvItemTitle;
        TextView tvItemLink;
        ImageView ivWebsiteLogo;

        public SearchResultsViewHolder(@NonNull View view) {
            super(view);
            cvSearchResult = view.findViewById(R.id.cvSearchResult);
            tvItemPrice = view.findViewById(R.id.tvItemPrice);
            tvItemTitle = view.findViewById(R.id.tvItemTitle);
            tvItemLink = view.findViewById(R.id.tvItemLink);
            ivWebsiteLogo = view.findViewById(R.id.ivWebsiteLogo);
        }
    }
}
