using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Clicklocation : MonoBehaviour {

    public double range = 1;
	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
        if (Input.GetMouseButtonDown(0))
        {
            Vector3 mouseVec = Input.mousePosition;

            

            float transformedx = (float)Math.Ceiling((mouseVec.x - 175) / 15.86);
            float transformedy = (float)Math.Ceiling((585-mouseVec.y) / 12);

            Vector3 mouseTran = new Vector3(transformedx, transformedy, 0);

            string mousePos = mouseTran.ToString();

            for (int i = 0; i < 2500; i++)
            {
                if (Uploadtextscript.x[i] != 0 && Uploadtextscript.y[i] != 0)
                {
                    if ((Uploadtextscript.x[i] - range) < mouseTran.x && mouseTran.x < (Uploadtextscript.x[i] + range))
                    {
                        if ((Uploadtextscript.y[i] - range) < mouseTran.y && mouseTran.y < (Uploadtextscript.y[i] + range))
                        {
                            GlobalControl.coins++;
                            GameObject.Find("Text").GetComponent<Text>().text = "Total Score = " + GlobalControl.coins;
                            Uploadtextscript.x[i] = 0;
                            Uploadtextscript.y[i] = 0;
                            Debug.Log("SCORE");
                        }
                    }
                }
                //Debug.Log("looped");
            }
            Debug.Log("CLICKED: " + mousePos);

        }
    }

    private void OnMouseDown()
    {
        
    }
}
