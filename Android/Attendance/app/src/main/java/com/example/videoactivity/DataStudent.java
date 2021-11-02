package com.example.videoactivity;

import android.net.Uri;

public class DataStudent {
    String name;
    String number;
    String temp;

    public DataStudent(String name, String number, String temp){
        this.name = name;
        this.number = number;
        this.temp = temp;
    }

    public String getName() { return name; }
    public void setName(String title) {
        this.name = name;
    }

    public String getNumer() {
        return number;
    }
    public void setNumber(String number) { this.number = number; }

    public String getTemp() {
        return temp;
    }
    public void setTemp(String temp) { this.temp = temp; }
}