using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public static class GlobalControl
{

    /// <summary>
    /// This script exists because these variables are accessed by multiple scripts and should be kept static.
    /// </summary> 

    public static float difficulty = 2;
    public static float score = 0;
    public static float roundscore = 0;
    public static float modifierx = 0;
    public static float modifiery = 0;
    public static float mute = 0;

}
