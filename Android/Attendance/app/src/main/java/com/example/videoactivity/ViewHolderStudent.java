package com.example.videoactivity;

import android.app.Dialog;
import android.net.Uri;
import android.util.Log;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AlertDialog;
import androidx.recyclerview.widget.GridLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.firestore.CollectionReference;
import com.google.firebase.firestore.DocumentSnapshot;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.QueryDocumentSnapshot;
import com.google.firebase.firestore.QuerySnapshot;
import com.google.firebase.firestore.auth.User;
import com.google.firebase.storage.FirebaseStorage;
import com.google.firebase.storage.StorageReference;

public class ViewHolderStudent extends RecyclerView.ViewHolder {

    TextView tv_student_title;
    TextView tv_student_number;
    TextView tv_student_temp;
    ImageView iv_student;
    String url; String name;

    public ViewHolderStudent(@NonNull View itemView) {
        super(itemView);

        iv_student = itemView.findViewById(R.id.iv_student);
        tv_student_title = itemView.findViewById(R.id.tv_student_title);
        tv_student_number = itemView.findViewById(R.id.tv_student_number);
        tv_student_temp = itemView.findViewById(R.id.tv_student_temp);

        // 아이템 클릭 이벤트 처리.
        itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // TODO : process click event.
                int pos = getAdapterPosition(); //몇번째 칸인지 알 수 있음
                showAlertDialogTopic();
            }
        });
    }

    public void onBind (DataStudent data){
        iv_student.setImageResource(R.drawable.hi);
        tv_student_title.setText(data.getName());
        tv_student_number.setText(data.getNumer());
        tv_student_temp.setText(data.getTemp());
        FirebaseStorage storage = FirebaseStorage.getInstance("gs://capstone-aae4f.appspot.com/");
        StorageReference storageRef = storage.getReference();
        name = (String) tv_student_title.getText();
        url = "/webcamCapture/" + name + "/faceCut.jpg";
        storageRef.child(url).getDownloadUrl().addOnSuccessListener(new OnSuccessListener<Uri>() {
            @Override
            public void onSuccess(Uri uri) {                //이미지 로드 성공시
                Glide.with(AttendanceActivity.context)
                        .load(uri)
                        .into(iv_student);
            }
        }).addOnFailureListener(new OnFailureListener() {
            @Override
            public void onFailure(@NonNull Exception exception) {                //이미지 로드 실패시
            }
        });
    }

    public void showAlertDialogTopic() {
        Dialog dialog = new Dialog(AttendanceActivity.context);

        dialog.setContentView(R.layout.custom_dialog);
        dialog.setTitle("Custom Dialog");

        ImageView iv = (ImageView) dialog.findViewById(R.id.image);
        iv.setImageResource(R.drawable.test);

        FirebaseStorage storage = FirebaseStorage.getInstance("gs://capstone-aae4f.appspot.com/");
        StorageReference storageRef = storage.getReference().child("webcamCapture");
        url = name + "/faceFull.jpg";
        storageRef.child(url).getDownloadUrl().addOnSuccessListener(new OnSuccessListener<Uri>() {
            @Override
            public void onSuccess(Uri uri) {
                //이미지 로드 성공시
                Glide.with(AttendanceActivity.context)
                        .load(uri)
                        .into(iv);
                Toast.makeText(AttendanceActivity.context, "dialog성공", Toast.LENGTH_SHORT).show();
            }
        }).addOnFailureListener(new OnFailureListener() {
            @Override
            public void onFailure(@NonNull Exception exception) {
                //이미지 로드 실패시
                Toast.makeText(AttendanceActivity.context, "dialog실패", Toast.LENGTH_SHORT).show();
            }
        });
        dialog.show();
    }
}