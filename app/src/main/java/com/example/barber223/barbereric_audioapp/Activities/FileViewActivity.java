//Eric Barber
//DVP6-1805
//FileViewActivity.java

package com.example.barber223.barbereric_audioapp.Activities;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import com.example.barber223.barbereric_audioapp.Fragments.Activity_Selection_Fragment_Top;
import com.example.barber223.barbereric_audioapp.Fragments.File_View_Fragement;
import com.example.barber223.barbereric_audioapp.Fragments.RecordInformationFragment;
import com.example.barber223.barbereric_audioapp.Interfaces.SelectionFragmentInterface;
import com.example.barber223.barbereric_audioapp.KeyClassHolder;
import com.example.barber223.barbereric_audioapp.R;

public class FileViewActivity extends AppCompatActivity implements SelectionFragmentInterface {

    private String activeDeviceProcess = KeyClassHolder.action_file;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_file_view);

        getFragmentManager().beginTransaction()
                .replace(R.id.activity_selection_fragment_frame, Activity_Selection_Fragment_Top.newInstance())
                .replace(R.id.files_fragment_frame, File_View_Fragement.newInstance())
                .replace(R.id.information_fragment_frame, RecordInformationFragment.newInstance())
                .commit();
    }

    @Override
    public void actionOfViewS(String _action) {
        activeDeviceProcess = _action;

        //need to load the new activity
        switch (_action){
            case KeyClassHolder.action_cloud:
                Intent newActivity = new Intent(this, CloudViewActivity.class);
                newActivity.setAction(KeyClassHolder.action_cloud);
                startActivity(newActivity);
                break;

            case KeyClassHolder.action_record:
                newActivity = new Intent(this, RecordMainActivity.class);
                newActivity.setAction(KeyClassHolder.action_record);
                startActivity(newActivity);
                break;
        }
        //This allows navigation between all of the activities and processes within the application
    }

    @Override
    public String getActiveProcess() {
        return activeDeviceProcess;
    }
}