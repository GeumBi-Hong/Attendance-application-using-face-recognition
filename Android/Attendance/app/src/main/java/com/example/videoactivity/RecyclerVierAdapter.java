package com.example.videoactivity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;

public class RecyclerVierAdapter extends RecyclerView.Adapter<RecyclerView.ViewHolder> {

    private final AttendanceActivity attendanceActivity;
    // adapter에 들어갈 list
    private ArrayList<DataStudent> listData = new ArrayList<>();
    public RecyclerVierAdapter(AttendanceActivity attendanceActivity, ArrayList<DataStudent> listData) {
        this.attendanceActivity = attendanceActivity;
        this.listData = listData;
    }

    @NonNull
    @Override
    public RecyclerView.ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_student, parent, false);
        return new ViewHolderStudent(view);
    }

    @Override
    public void onBindViewHolder(@NonNull RecyclerView.ViewHolder holder, int position) {
        ((ViewHolderStudent)holder).onBind(listData.get(position));
    }

    @Override
    public int getItemCount() {
        return listData.size();
    }

    void addItem(DataStudent data) {
        listData.add(data);
    }
}
