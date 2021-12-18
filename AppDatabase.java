package #pak#.db;

import android.content.Context;
import androidx.room.Database;
import androidx.room.Room;
import androidx.room.RoomDatabase;
import androidx.room.TypeConverters;
#import_dao#
#import_entity#

@Database(entities = {#clss#}, version = 1, exportSchema = false)
@TypeConverters({RoomConverter.class})
public abstract class AppDatabase extends RoomDatabase {

    static String dbFileName = "whatRubbish.db";
    #def#
   
    private static volatile AppDatabase INSTANCE;

    public static AppDatabase getDatabase(Context context) {
        if (INSTANCE == null) {
            synchronized (AppDatabase.class) {
                if (INSTANCE == null) {
                    INSTANCE = Room.databaseBuilder(context, AppDatabase.class, dbFileName)
                            .fallbackToDestructiveMigration()
                            .build();
                }
            }
        }
        return INSTANCE;
    }
}
