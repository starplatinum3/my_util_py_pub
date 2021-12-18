package com.example.whatrubbish.db;

import android.content.Context;
#import#
import lombok.Data;

@Data
public class Repository {

    Context context;
    AppDatabase database;
    #def#

    public Repository(Context context) {
        this.context = context;
        initDatabase(context);
    }

    void initDatabase(Context context) {
        if (database == null) {
            database = AppDatabase.getDatabase(context);
        }
        #new#
    }
}
