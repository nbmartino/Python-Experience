
#include <Python.h>
#ifdef __FreeBSD__
#include <dev/evdev/input.h>
#else
#include <linux/input.h>
#endif

/* Automatically generated by evdev.genecodes */
/* Generated on Linux 3.12.28+ #709 PREEMPT Mon Sep 8 15:28:00 BST 2014 armv6l */

#define MODULE_NAME "_ecodes"
#define MODULE_HELP "linux/input.h macros"

static PyMethodDef MethodTable[] = {
    { NULL, NULL, 0, NULL}
};

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    MODULE_NAME,
    MODULE_HELP,
    -1,          /* m_size */
    MethodTable, /* m_methods */
    NULL,        /* m_reload */
    NULL,        /* m_traverse */
    NULL,        /* m_clear */
    NULL,        /* m_free */
};
#endif

static PyObject *
moduleinit(void)
{

#if PY_MAJOR_VERSION >= 3
    PyObject* m = PyModule_Create(&moduledef);
#else
    PyObject* m = Py_InitModule3(MODULE_NAME, MethodTable, MODULE_HELP);
#endif

    if (m == NULL) return NULL;

    PyModule_AddIntMacro(m, EV_VERSION);
    PyModule_AddIntMacro(m, EV_SYN);
    PyModule_AddIntMacro(m, EV_KEY);
    PyModule_AddIntMacro(m, EV_REL);
    PyModule_AddIntMacro(m, EV_ABS);
    PyModule_AddIntMacro(m, EV_MSC);
    PyModule_AddIntMacro(m, EV_SW);
    PyModule_AddIntMacro(m, EV_LED);
    PyModule_AddIntMacro(m, EV_SND);
    PyModule_AddIntMacro(m, EV_REP);
    PyModule_AddIntMacro(m, EV_FF);
    PyModule_AddIntMacro(m, EV_PWR);
    PyModule_AddIntMacro(m, EV_FF_STATUS);
    PyModule_AddIntMacro(m, EV_MAX);
    PyModule_AddIntMacro(m, EV_CNT);
    PyModule_AddIntMacro(m, SYN_REPORT);
    PyModule_AddIntMacro(m, SYN_CONFIG);
    PyModule_AddIntMacro(m, SYN_MT_REPORT);
    PyModule_AddIntMacro(m, SYN_DROPPED);
    PyModule_AddIntMacro(m, KEY_RESERVED);
    PyModule_AddIntMacro(m, KEY_ESC);
    PyModule_AddIntMacro(m, KEY_1);
    PyModule_AddIntMacro(m, KEY_2);
    PyModule_AddIntMacro(m, KEY_3);
    PyModule_AddIntMacro(m, KEY_4);
    PyModule_AddIntMacro(m, KEY_5);
    PyModule_AddIntMacro(m, KEY_6);
    PyModule_AddIntMacro(m, KEY_7);
    PyModule_AddIntMacro(m, KEY_8);
    PyModule_AddIntMacro(m, KEY_9);
    PyModule_AddIntMacro(m, KEY_0);
    PyModule_AddIntMacro(m, KEY_MINUS);
    PyModule_AddIntMacro(m, KEY_EQUAL);
    PyModule_AddIntMacro(m, KEY_BACKSPACE);
    PyModule_AddIntMacro(m, KEY_TAB);
    PyModule_AddIntMacro(m, KEY_Q);
    PyModule_AddIntMacro(m, KEY_W);
    PyModule_AddIntMacro(m, KEY_E);
    PyModule_AddIntMacro(m, KEY_R);
    PyModule_AddIntMacro(m, KEY_T);
    PyModule_AddIntMacro(m, KEY_Y);
    PyModule_AddIntMacro(m, KEY_U);
    PyModule_AddIntMacro(m, KEY_I);
    PyModule_AddIntMacro(m, KEY_O);
    PyModule_AddIntMacro(m, KEY_P);
    PyModule_AddIntMacro(m, KEY_LEFTBRACE);
    PyModule_AddIntMacro(m, KEY_RIGHTBRACE);
    PyModule_AddIntMacro(m, KEY_ENTER);
    PyModule_AddIntMacro(m, KEY_LEFTCTRL);
    PyModule_AddIntMacro(m, KEY_A);
    PyModule_AddIntMacro(m, KEY_S);
    PyModule_AddIntMacro(m, KEY_D);
    PyModule_AddIntMacro(m, KEY_F);
    PyModule_AddIntMacro(m, KEY_G);
    PyModule_AddIntMacro(m, KEY_H);
    PyModule_AddIntMacro(m, KEY_J);
    PyModule_AddIntMacro(m, KEY_K);
    PyModule_AddIntMacro(m, KEY_L);
    PyModule_AddIntMacro(m, KEY_SEMICOLON);
    PyModule_AddIntMacro(m, KEY_APOSTROPHE);
    PyModule_AddIntMacro(m, KEY_GRAVE);
    PyModule_AddIntMacro(m, KEY_LEFTSHIFT);
    PyModule_AddIntMacro(m, KEY_BACKSLASH);
    PyModule_AddIntMacro(m, KEY_Z);
    PyModule_AddIntMacro(m, KEY_X);
    PyModule_AddIntMacro(m, KEY_C);
    PyModule_AddIntMacro(m, KEY_V);
    PyModule_AddIntMacro(m, KEY_B);
    PyModule_AddIntMacro(m, KEY_N);
    PyModule_AddIntMacro(m, KEY_M);
    PyModule_AddIntMacro(m, KEY_COMMA);
    PyModule_AddIntMacro(m, KEY_DOT);
    PyModule_AddIntMacro(m, KEY_SLASH);
    PyModule_AddIntMacro(m, KEY_RIGHTSHIFT);
    PyModule_AddIntMacro(m, KEY_KPASTERISK);
    PyModule_AddIntMacro(m, KEY_LEFTALT);
    PyModule_AddIntMacro(m, KEY_SPACE);
    PyModule_AddIntMacro(m, KEY_CAPSLOCK);
    PyModule_AddIntMacro(m, KEY_F1);
    PyModule_AddIntMacro(m, KEY_F2);
    PyModule_AddIntMacro(m, KEY_F3);
    PyModule_AddIntMacro(m, KEY_F4);
    PyModule_AddIntMacro(m, KEY_F5);
    PyModule_AddIntMacro(m, KEY_F6);
    PyModule_AddIntMacro(m, KEY_F7);
    PyModule_AddIntMacro(m, KEY_F8);
    PyModule_AddIntMacro(m, KEY_F9);
    PyModule_AddIntMacro(m, KEY_F10);
    PyModule_AddIntMacro(m, KEY_NUMLOCK);
    PyModule_AddIntMacro(m, KEY_SCROLLLOCK);
    PyModule_AddIntMacro(m, KEY_KP7);
    PyModule_AddIntMacro(m, KEY_KP8);
    PyModule_AddIntMacro(m, KEY_KP9);
    PyModule_AddIntMacro(m, KEY_KPMINUS);
    PyModule_AddIntMacro(m, KEY_KP4);
    PyModule_AddIntMacro(m, KEY_KP5);
    PyModule_AddIntMacro(m, KEY_KP6);
    PyModule_AddIntMacro(m, KEY_KPPLUS);
    PyModule_AddIntMacro(m, KEY_KP1);
    PyModule_AddIntMacro(m, KEY_KP2);
    PyModule_AddIntMacro(m, KEY_KP3);
    PyModule_AddIntMacro(m, KEY_KP0);
    PyModule_AddIntMacro(m, KEY_KPDOT);
    PyModule_AddIntMacro(m, KEY_ZENKAKUHANKAKU);
    PyModule_AddIntMacro(m, KEY_102ND);
    PyModule_AddIntMacro(m, KEY_F11);
    PyModule_AddIntMacro(m, KEY_F12);
    PyModule_AddIntMacro(m, KEY_RO);
    PyModule_AddIntMacro(m, KEY_KATAKANA);
    PyModule_AddIntMacro(m, KEY_HIRAGANA);
    PyModule_AddIntMacro(m, KEY_HENKAN);
    PyModule_AddIntMacro(m, KEY_KATAKANAHIRAGANA);
    PyModule_AddIntMacro(m, KEY_MUHENKAN);
    PyModule_AddIntMacro(m, KEY_KPJPCOMMA);
    PyModule_AddIntMacro(m, KEY_KPENTER);
    PyModule_AddIntMacro(m, KEY_RIGHTCTRL);
    PyModule_AddIntMacro(m, KEY_KPSLASH);
    PyModule_AddIntMacro(m, KEY_SYSRQ);
    PyModule_AddIntMacro(m, KEY_RIGHTALT);
    PyModule_AddIntMacro(m, KEY_LINEFEED);
    PyModule_AddIntMacro(m, KEY_HOME);
    PyModule_AddIntMacro(m, KEY_UP);
    PyModule_AddIntMacro(m, KEY_PAGEUP);
    PyModule_AddIntMacro(m, KEY_LEFT);
    PyModule_AddIntMacro(m, KEY_RIGHT);
    PyModule_AddIntMacro(m, KEY_END);
    PyModule_AddIntMacro(m, KEY_DOWN);
    PyModule_AddIntMacro(m, KEY_PAGEDOWN);
    PyModule_AddIntMacro(m, KEY_INSERT);
    PyModule_AddIntMacro(m, KEY_DELETE);
    PyModule_AddIntMacro(m, KEY_MACRO);
    PyModule_AddIntMacro(m, KEY_MUTE);
    PyModule_AddIntMacro(m, KEY_VOLUMEDOWN);
    PyModule_AddIntMacro(m, KEY_VOLUMEUP);
    PyModule_AddIntMacro(m, KEY_POWER);
    PyModule_AddIntMacro(m, KEY_KPEQUAL);
    PyModule_AddIntMacro(m, KEY_KPPLUSMINUS);
    PyModule_AddIntMacro(m, KEY_PAUSE);
    PyModule_AddIntMacro(m, KEY_SCALE);
    PyModule_AddIntMacro(m, KEY_KPCOMMA);
    PyModule_AddIntMacro(m, KEY_HANGEUL);
    PyModule_AddIntMacro(m, KEY_HANGUEL);
    PyModule_AddIntMacro(m, KEY_HANJA);
    PyModule_AddIntMacro(m, KEY_YEN);
    PyModule_AddIntMacro(m, KEY_LEFTMETA);
    PyModule_AddIntMacro(m, KEY_RIGHTMETA);
    PyModule_AddIntMacro(m, KEY_COMPOSE);
    PyModule_AddIntMacro(m, KEY_STOP);
    PyModule_AddIntMacro(m, KEY_AGAIN);
    PyModule_AddIntMacro(m, KEY_PROPS);
    PyModule_AddIntMacro(m, KEY_UNDO);
    PyModule_AddIntMacro(m, KEY_FRONT);
    PyModule_AddIntMacro(m, KEY_COPY);
    PyModule_AddIntMacro(m, KEY_OPEN);
    PyModule_AddIntMacro(m, KEY_PASTE);
    PyModule_AddIntMacro(m, KEY_FIND);
    PyModule_AddIntMacro(m, KEY_CUT);
    PyModule_AddIntMacro(m, KEY_HELP);
    PyModule_AddIntMacro(m, KEY_MENU);
    PyModule_AddIntMacro(m, KEY_CALC);
    PyModule_AddIntMacro(m, KEY_SETUP);
    PyModule_AddIntMacro(m, KEY_SLEEP);
    PyModule_AddIntMacro(m, KEY_WAKEUP);
    PyModule_AddIntMacro(m, KEY_FILE);
    PyModule_AddIntMacro(m, KEY_SENDFILE);
    PyModule_AddIntMacro(m, KEY_DELETEFILE);
    PyModule_AddIntMacro(m, KEY_XFER);
    PyModule_AddIntMacro(m, KEY_PROG1);
    PyModule_AddIntMacro(m, KEY_PROG2);
    PyModule_AddIntMacro(m, KEY_WWW);
    PyModule_AddIntMacro(m, KEY_MSDOS);
    PyModule_AddIntMacro(m, KEY_COFFEE);
    PyModule_AddIntMacro(m, KEY_SCREENLOCK);
    PyModule_AddIntMacro(m, KEY_DIRECTION);
    PyModule_AddIntMacro(m, KEY_CYCLEWINDOWS);
    PyModule_AddIntMacro(m, KEY_MAIL);
    PyModule_AddIntMacro(m, KEY_BOOKMARKS);
    PyModule_AddIntMacro(m, KEY_COMPUTER);
    PyModule_AddIntMacro(m, KEY_BACK);
    PyModule_AddIntMacro(m, KEY_FORWARD);
    PyModule_AddIntMacro(m, KEY_CLOSECD);
    PyModule_AddIntMacro(m, KEY_EJECTCD);
    PyModule_AddIntMacro(m, KEY_EJECTCLOSECD);
    PyModule_AddIntMacro(m, KEY_NEXTSONG);
    PyModule_AddIntMacro(m, KEY_PLAYPAUSE);
    PyModule_AddIntMacro(m, KEY_PREVIOUSSONG);
    PyModule_AddIntMacro(m, KEY_STOPCD);
    PyModule_AddIntMacro(m, KEY_RECORD);
    PyModule_AddIntMacro(m, KEY_REWIND);
    PyModule_AddIntMacro(m, KEY_PHONE);
    PyModule_AddIntMacro(m, KEY_ISO);
    PyModule_AddIntMacro(m, KEY_CONFIG);
    PyModule_AddIntMacro(m, KEY_HOMEPAGE);
    PyModule_AddIntMacro(m, KEY_REFRESH);
    PyModule_AddIntMacro(m, KEY_EXIT);
    PyModule_AddIntMacro(m, KEY_MOVE);
    PyModule_AddIntMacro(m, KEY_EDIT);
    PyModule_AddIntMacro(m, KEY_SCROLLUP);
    PyModule_AddIntMacro(m, KEY_SCROLLDOWN);
    PyModule_AddIntMacro(m, KEY_KPLEFTPAREN);
    PyModule_AddIntMacro(m, KEY_KPRIGHTPAREN);
    PyModule_AddIntMacro(m, KEY_NEW);
    PyModule_AddIntMacro(m, KEY_REDO);
    PyModule_AddIntMacro(m, KEY_F13);
    PyModule_AddIntMacro(m, KEY_F14);
    PyModule_AddIntMacro(m, KEY_F15);
    PyModule_AddIntMacro(m, KEY_F16);
    PyModule_AddIntMacro(m, KEY_F17);
    PyModule_AddIntMacro(m, KEY_F18);
    PyModule_AddIntMacro(m, KEY_F19);
    PyModule_AddIntMacro(m, KEY_F20);
    PyModule_AddIntMacro(m, KEY_F21);
    PyModule_AddIntMacro(m, KEY_F22);
    PyModule_AddIntMacro(m, KEY_F23);
    PyModule_AddIntMacro(m, KEY_F24);
    PyModule_AddIntMacro(m, KEY_PLAYCD);
    PyModule_AddIntMacro(m, KEY_PAUSECD);
    PyModule_AddIntMacro(m, KEY_PROG3);
    PyModule_AddIntMacro(m, KEY_PROG4);
    PyModule_AddIntMacro(m, KEY_DASHBOARD);
    PyModule_AddIntMacro(m, KEY_SUSPEND);
    PyModule_AddIntMacro(m, KEY_CLOSE);
    PyModule_AddIntMacro(m, KEY_PLAY);
    PyModule_AddIntMacro(m, KEY_FASTFORWARD);
    PyModule_AddIntMacro(m, KEY_BASSBOOST);
    PyModule_AddIntMacro(m, KEY_PRINT);
    PyModule_AddIntMacro(m, KEY_HP);
    PyModule_AddIntMacro(m, KEY_CAMERA);
    PyModule_AddIntMacro(m, KEY_SOUND);
    PyModule_AddIntMacro(m, KEY_QUESTION);
    PyModule_AddIntMacro(m, KEY_EMAIL);
    PyModule_AddIntMacro(m, KEY_CHAT);
    PyModule_AddIntMacro(m, KEY_SEARCH);
    PyModule_AddIntMacro(m, KEY_CONNECT);
    PyModule_AddIntMacro(m, KEY_FINANCE);
    PyModule_AddIntMacro(m, KEY_SPORT);
    PyModule_AddIntMacro(m, KEY_SHOP);
    PyModule_AddIntMacro(m, KEY_ALTERASE);
    PyModule_AddIntMacro(m, KEY_CANCEL);
    PyModule_AddIntMacro(m, KEY_BRIGHTNESSDOWN);
    PyModule_AddIntMacro(m, KEY_BRIGHTNESSUP);
    PyModule_AddIntMacro(m, KEY_MEDIA);
    PyModule_AddIntMacro(m, KEY_SWITCHVIDEOMODE);
    PyModule_AddIntMacro(m, KEY_KBDILLUMTOGGLE);
    PyModule_AddIntMacro(m, KEY_KBDILLUMDOWN);
    PyModule_AddIntMacro(m, KEY_KBDILLUMUP);
    PyModule_AddIntMacro(m, KEY_SEND);
    PyModule_AddIntMacro(m, KEY_REPLY);
    PyModule_AddIntMacro(m, KEY_FORWARDMAIL);
    PyModule_AddIntMacro(m, KEY_SAVE);
    PyModule_AddIntMacro(m, KEY_DOCUMENTS);
    PyModule_AddIntMacro(m, KEY_BATTERY);
    PyModule_AddIntMacro(m, KEY_BLUETOOTH);
    PyModule_AddIntMacro(m, KEY_WLAN);
    PyModule_AddIntMacro(m, KEY_UWB);
    PyModule_AddIntMacro(m, KEY_UNKNOWN);
    PyModule_AddIntMacro(m, KEY_VIDEO_NEXT);
    PyModule_AddIntMacro(m, KEY_VIDEO_PREV);
    PyModule_AddIntMacro(m, KEY_BRIGHTNESS_CYCLE);
    PyModule_AddIntMacro(m, KEY_BRIGHTNESS_ZERO);
    PyModule_AddIntMacro(m, KEY_DISPLAY_OFF);
    PyModule_AddIntMacro(m, KEY_WIMAX);
    PyModule_AddIntMacro(m, KEY_RFKILL);
    PyModule_AddIntMacro(m, KEY_MICMUTE);
    PyModule_AddIntMacro(m, BTN_MISC);
    PyModule_AddIntMacro(m, BTN_0);
    PyModule_AddIntMacro(m, BTN_1);
    PyModule_AddIntMacro(m, BTN_2);
    PyModule_AddIntMacro(m, BTN_3);
    PyModule_AddIntMacro(m, BTN_4);
    PyModule_AddIntMacro(m, BTN_5);
    PyModule_AddIntMacro(m, BTN_6);
    PyModule_AddIntMacro(m, BTN_7);
    PyModule_AddIntMacro(m, BTN_8);
    PyModule_AddIntMacro(m, BTN_9);
    PyModule_AddIntMacro(m, BTN_MOUSE);
    PyModule_AddIntMacro(m, BTN_LEFT);
    PyModule_AddIntMacro(m, BTN_RIGHT);
    PyModule_AddIntMacro(m, BTN_MIDDLE);
    PyModule_AddIntMacro(m, BTN_SIDE);
    PyModule_AddIntMacro(m, BTN_EXTRA);
    PyModule_AddIntMacro(m, BTN_FORWARD);
    PyModule_AddIntMacro(m, BTN_BACK);
    PyModule_AddIntMacro(m, BTN_TASK);
    PyModule_AddIntMacro(m, BTN_JOYSTICK);
    PyModule_AddIntMacro(m, BTN_TRIGGER);
    PyModule_AddIntMacro(m, BTN_THUMB);
    PyModule_AddIntMacro(m, BTN_THUMB2);
    PyModule_AddIntMacro(m, BTN_TOP);
    PyModule_AddIntMacro(m, BTN_TOP2);
    PyModule_AddIntMacro(m, BTN_PINKIE);
    PyModule_AddIntMacro(m, BTN_BASE);
    PyModule_AddIntMacro(m, BTN_BASE2);
    PyModule_AddIntMacro(m, BTN_BASE3);
    PyModule_AddIntMacro(m, BTN_BASE4);
    PyModule_AddIntMacro(m, BTN_BASE5);
    PyModule_AddIntMacro(m, BTN_BASE6);
    PyModule_AddIntMacro(m, BTN_DEAD);
    PyModule_AddIntMacro(m, BTN_GAMEPAD);
    PyModule_AddIntMacro(m, BTN_A);
    PyModule_AddIntMacro(m, BTN_B);
    PyModule_AddIntMacro(m, BTN_C);
    PyModule_AddIntMacro(m, BTN_X);
    PyModule_AddIntMacro(m, BTN_Y);
    PyModule_AddIntMacro(m, BTN_Z);
    PyModule_AddIntMacro(m, BTN_TL);
    PyModule_AddIntMacro(m, BTN_TR);
    PyModule_AddIntMacro(m, BTN_TL2);
    PyModule_AddIntMacro(m, BTN_TR2);
    PyModule_AddIntMacro(m, BTN_SELECT);
    PyModule_AddIntMacro(m, BTN_START);
    PyModule_AddIntMacro(m, BTN_MODE);
    PyModule_AddIntMacro(m, BTN_THUMBL);
    PyModule_AddIntMacro(m, BTN_THUMBR);
    PyModule_AddIntMacro(m, BTN_DIGI);
    PyModule_AddIntMacro(m, BTN_TOOL_PEN);
    PyModule_AddIntMacro(m, BTN_TOOL_RUBBER);
    PyModule_AddIntMacro(m, BTN_TOOL_BRUSH);
    PyModule_AddIntMacro(m, BTN_TOOL_PENCIL);
    PyModule_AddIntMacro(m, BTN_TOOL_AIRBRUSH);
    PyModule_AddIntMacro(m, BTN_TOOL_FINGER);
    PyModule_AddIntMacro(m, BTN_TOOL_MOUSE);
    PyModule_AddIntMacro(m, BTN_TOOL_LENS);
    PyModule_AddIntMacro(m, BTN_TOOL_QUINTTAP);
    PyModule_AddIntMacro(m, BTN_TOUCH);
    PyModule_AddIntMacro(m, BTN_STYLUS);
    PyModule_AddIntMacro(m, BTN_STYLUS2);
    PyModule_AddIntMacro(m, BTN_TOOL_DOUBLETAP);
    PyModule_AddIntMacro(m, BTN_TOOL_TRIPLETAP);
    PyModule_AddIntMacro(m, BTN_TOOL_QUADTAP);
    PyModule_AddIntMacro(m, BTN_WHEEL);
    PyModule_AddIntMacro(m, BTN_GEAR_DOWN);
    PyModule_AddIntMacro(m, BTN_GEAR_UP);
    PyModule_AddIntMacro(m, KEY_OK);
    PyModule_AddIntMacro(m, KEY_SELECT);
    PyModule_AddIntMacro(m, KEY_GOTO);
    PyModule_AddIntMacro(m, KEY_CLEAR);
    PyModule_AddIntMacro(m, KEY_POWER2);
    PyModule_AddIntMacro(m, KEY_OPTION);
    PyModule_AddIntMacro(m, KEY_INFO);
    PyModule_AddIntMacro(m, KEY_TIME);
    PyModule_AddIntMacro(m, KEY_VENDOR);
    PyModule_AddIntMacro(m, KEY_ARCHIVE);
    PyModule_AddIntMacro(m, KEY_PROGRAM);
    PyModule_AddIntMacro(m, KEY_CHANNEL);
    PyModule_AddIntMacro(m, KEY_FAVORITES);
    PyModule_AddIntMacro(m, KEY_EPG);
    PyModule_AddIntMacro(m, KEY_PVR);
    PyModule_AddIntMacro(m, KEY_MHP);
    PyModule_AddIntMacro(m, KEY_LANGUAGE);
    PyModule_AddIntMacro(m, KEY_TITLE);
    PyModule_AddIntMacro(m, KEY_SUBTITLE);
    PyModule_AddIntMacro(m, KEY_ANGLE);
    PyModule_AddIntMacro(m, KEY_ZOOM);
    PyModule_AddIntMacro(m, KEY_MODE);
    PyModule_AddIntMacro(m, KEY_KEYBOARD);
    PyModule_AddIntMacro(m, KEY_SCREEN);
    PyModule_AddIntMacro(m, KEY_PC);
    PyModule_AddIntMacro(m, KEY_TV);
    PyModule_AddIntMacro(m, KEY_TV2);
    PyModule_AddIntMacro(m, KEY_VCR);
    PyModule_AddIntMacro(m, KEY_VCR2);
    PyModule_AddIntMacro(m, KEY_SAT);
    PyModule_AddIntMacro(m, KEY_SAT2);
    PyModule_AddIntMacro(m, KEY_CD);
    PyModule_AddIntMacro(m, KEY_TAPE);
    PyModule_AddIntMacro(m, KEY_RADIO);
    PyModule_AddIntMacro(m, KEY_TUNER);
    PyModule_AddIntMacro(m, KEY_PLAYER);
    PyModule_AddIntMacro(m, KEY_TEXT);
    PyModule_AddIntMacro(m, KEY_DVD);
    PyModule_AddIntMacro(m, KEY_AUX);
    PyModule_AddIntMacro(m, KEY_MP3);
    PyModule_AddIntMacro(m, KEY_AUDIO);
    PyModule_AddIntMacro(m, KEY_VIDEO);
    PyModule_AddIntMacro(m, KEY_DIRECTORY);
    PyModule_AddIntMacro(m, KEY_LIST);
    PyModule_AddIntMacro(m, KEY_MEMO);
    PyModule_AddIntMacro(m, KEY_CALENDAR);
    PyModule_AddIntMacro(m, KEY_RED);
    PyModule_AddIntMacro(m, KEY_GREEN);
    PyModule_AddIntMacro(m, KEY_YELLOW);
    PyModule_AddIntMacro(m, KEY_BLUE);
    PyModule_AddIntMacro(m, KEY_CHANNELUP);
    PyModule_AddIntMacro(m, KEY_CHANNELDOWN);
    PyModule_AddIntMacro(m, KEY_FIRST);
    PyModule_AddIntMacro(m, KEY_LAST);
    PyModule_AddIntMacro(m, KEY_AB);
    PyModule_AddIntMacro(m, KEY_NEXT);
    PyModule_AddIntMacro(m, KEY_RESTART);
    PyModule_AddIntMacro(m, KEY_SLOW);
    PyModule_AddIntMacro(m, KEY_SHUFFLE);
    PyModule_AddIntMacro(m, KEY_BREAK);
    PyModule_AddIntMacro(m, KEY_PREVIOUS);
    PyModule_AddIntMacro(m, KEY_DIGITS);
    PyModule_AddIntMacro(m, KEY_TEEN);
    PyModule_AddIntMacro(m, KEY_TWEN);
    PyModule_AddIntMacro(m, KEY_VIDEOPHONE);
    PyModule_AddIntMacro(m, KEY_GAMES);
    PyModule_AddIntMacro(m, KEY_ZOOMIN);
    PyModule_AddIntMacro(m, KEY_ZOOMOUT);
    PyModule_AddIntMacro(m, KEY_ZOOMRESET);
    PyModule_AddIntMacro(m, KEY_WORDPROCESSOR);
    PyModule_AddIntMacro(m, KEY_EDITOR);
    PyModule_AddIntMacro(m, KEY_SPREADSHEET);
    PyModule_AddIntMacro(m, KEY_GRAPHICSEDITOR);
    PyModule_AddIntMacro(m, KEY_PRESENTATION);
    PyModule_AddIntMacro(m, KEY_DATABASE);
    PyModule_AddIntMacro(m, KEY_NEWS);
    PyModule_AddIntMacro(m, KEY_VOICEMAIL);
    PyModule_AddIntMacro(m, KEY_ADDRESSBOOK);
    PyModule_AddIntMacro(m, KEY_MESSENGER);
    PyModule_AddIntMacro(m, KEY_DISPLAYTOGGLE);
    PyModule_AddIntMacro(m, KEY_SPELLCHECK);
    PyModule_AddIntMacro(m, KEY_LOGOFF);
    PyModule_AddIntMacro(m, KEY_DOLLAR);
    PyModule_AddIntMacro(m, KEY_EURO);
    PyModule_AddIntMacro(m, KEY_FRAMEBACK);
    PyModule_AddIntMacro(m, KEY_FRAMEFORWARD);
    PyModule_AddIntMacro(m, KEY_CONTEXT_MENU);
    PyModule_AddIntMacro(m, KEY_MEDIA_REPEAT);
    PyModule_AddIntMacro(m, KEY_10CHANNELSUP);
    PyModule_AddIntMacro(m, KEY_10CHANNELSDOWN);
    PyModule_AddIntMacro(m, KEY_IMAGES);
    PyModule_AddIntMacro(m, KEY_DEL_EOL);
    PyModule_AddIntMacro(m, KEY_DEL_EOS);
    PyModule_AddIntMacro(m, KEY_INS_LINE);
    PyModule_AddIntMacro(m, KEY_DEL_LINE);
    PyModule_AddIntMacro(m, KEY_FN);
    PyModule_AddIntMacro(m, KEY_FN_ESC);
    PyModule_AddIntMacro(m, KEY_FN_F1);
    PyModule_AddIntMacro(m, KEY_FN_F2);
    PyModule_AddIntMacro(m, KEY_FN_F3);
    PyModule_AddIntMacro(m, KEY_FN_F4);
    PyModule_AddIntMacro(m, KEY_FN_F5);
    PyModule_AddIntMacro(m, KEY_FN_F6);
    PyModule_AddIntMacro(m, KEY_FN_F7);
    PyModule_AddIntMacro(m, KEY_FN_F8);
    PyModule_AddIntMacro(m, KEY_FN_F9);
    PyModule_AddIntMacro(m, KEY_FN_F10);
    PyModule_AddIntMacro(m, KEY_FN_F11);
    PyModule_AddIntMacro(m, KEY_FN_F12);
    PyModule_AddIntMacro(m, KEY_FN_1);
    PyModule_AddIntMacro(m, KEY_FN_2);
    PyModule_AddIntMacro(m, KEY_FN_D);
    PyModule_AddIntMacro(m, KEY_FN_E);
    PyModule_AddIntMacro(m, KEY_FN_F);
    PyModule_AddIntMacro(m, KEY_FN_S);
    PyModule_AddIntMacro(m, KEY_FN_B);
    PyModule_AddIntMacro(m, KEY_BRL_DOT1);
    PyModule_AddIntMacro(m, KEY_BRL_DOT2);
    PyModule_AddIntMacro(m, KEY_BRL_DOT3);
    PyModule_AddIntMacro(m, KEY_BRL_DOT4);
    PyModule_AddIntMacro(m, KEY_BRL_DOT5);
    PyModule_AddIntMacro(m, KEY_BRL_DOT6);
    PyModule_AddIntMacro(m, KEY_BRL_DOT7);
    PyModule_AddIntMacro(m, KEY_BRL_DOT8);
    PyModule_AddIntMacro(m, KEY_BRL_DOT9);
    PyModule_AddIntMacro(m, KEY_BRL_DOT10);
    PyModule_AddIntMacro(m, KEY_NUMERIC_0);
    PyModule_AddIntMacro(m, KEY_NUMERIC_1);
    PyModule_AddIntMacro(m, KEY_NUMERIC_2);
    PyModule_AddIntMacro(m, KEY_NUMERIC_3);
    PyModule_AddIntMacro(m, KEY_NUMERIC_4);
    PyModule_AddIntMacro(m, KEY_NUMERIC_5);
    PyModule_AddIntMacro(m, KEY_NUMERIC_6);
    PyModule_AddIntMacro(m, KEY_NUMERIC_7);
    PyModule_AddIntMacro(m, KEY_NUMERIC_8);
    PyModule_AddIntMacro(m, KEY_NUMERIC_9);
    PyModule_AddIntMacro(m, KEY_NUMERIC_STAR);
    PyModule_AddIntMacro(m, KEY_NUMERIC_POUND);
    PyModule_AddIntMacro(m, KEY_CAMERA_FOCUS);
    PyModule_AddIntMacro(m, KEY_WPS_BUTTON);
    PyModule_AddIntMacro(m, KEY_TOUCHPAD_TOGGLE);
    PyModule_AddIntMacro(m, KEY_TOUCHPAD_ON);
    PyModule_AddIntMacro(m, KEY_TOUCHPAD_OFF);
    PyModule_AddIntMacro(m, KEY_CAMERA_ZOOMIN);
    PyModule_AddIntMacro(m, KEY_CAMERA_ZOOMOUT);
    PyModule_AddIntMacro(m, KEY_CAMERA_UP);
    PyModule_AddIntMacro(m, KEY_CAMERA_DOWN);
    PyModule_AddIntMacro(m, KEY_CAMERA_LEFT);
    PyModule_AddIntMacro(m, KEY_CAMERA_RIGHT);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY1);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY2);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY3);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY4);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY5);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY6);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY7);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY8);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY9);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY10);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY11);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY12);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY13);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY14);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY15);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY16);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY17);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY18);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY19);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY20);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY21);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY22);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY23);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY24);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY25);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY26);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY27);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY28);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY29);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY30);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY31);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY32);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY33);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY34);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY35);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY36);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY37);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY38);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY39);
    PyModule_AddIntMacro(m, BTN_TRIGGER_HAPPY40);
    PyModule_AddIntMacro(m, KEY_MIN_INTERESTING);
    PyModule_AddIntMacro(m, KEY_MAX);
    PyModule_AddIntMacro(m, KEY_CNT);
    PyModule_AddIntMacro(m, REL_X);
    PyModule_AddIntMacro(m, REL_Y);
    PyModule_AddIntMacro(m, REL_Z);
    PyModule_AddIntMacro(m, REL_RX);
    PyModule_AddIntMacro(m, REL_RY);
    PyModule_AddIntMacro(m, REL_RZ);
    PyModule_AddIntMacro(m, REL_HWHEEL);
    PyModule_AddIntMacro(m, REL_DIAL);
    PyModule_AddIntMacro(m, REL_WHEEL);
    PyModule_AddIntMacro(m, REL_MISC);
    PyModule_AddIntMacro(m, REL_MAX);
    PyModule_AddIntMacro(m, REL_CNT);
    PyModule_AddIntMacro(m, ABS_X);
    PyModule_AddIntMacro(m, ABS_Y);
    PyModule_AddIntMacro(m, ABS_Z);
    PyModule_AddIntMacro(m, ABS_RX);
    PyModule_AddIntMacro(m, ABS_RY);
    PyModule_AddIntMacro(m, ABS_RZ);
    PyModule_AddIntMacro(m, ABS_THROTTLE);
    PyModule_AddIntMacro(m, ABS_RUDDER);
    PyModule_AddIntMacro(m, ABS_WHEEL);
    PyModule_AddIntMacro(m, ABS_GAS);
    PyModule_AddIntMacro(m, ABS_BRAKE);
    PyModule_AddIntMacro(m, ABS_HAT0X);
    PyModule_AddIntMacro(m, ABS_HAT0Y);
    PyModule_AddIntMacro(m, ABS_HAT1X);
    PyModule_AddIntMacro(m, ABS_HAT1Y);
    PyModule_AddIntMacro(m, ABS_HAT2X);
    PyModule_AddIntMacro(m, ABS_HAT2Y);
    PyModule_AddIntMacro(m, ABS_HAT3X);
    PyModule_AddIntMacro(m, ABS_HAT3Y);
    PyModule_AddIntMacro(m, ABS_PRESSURE);
    PyModule_AddIntMacro(m, ABS_DISTANCE);
    PyModule_AddIntMacro(m, ABS_TILT_X);
    PyModule_AddIntMacro(m, ABS_TILT_Y);
    PyModule_AddIntMacro(m, ABS_TOOL_WIDTH);
    PyModule_AddIntMacro(m, ABS_VOLUME);
    PyModule_AddIntMacro(m, ABS_MISC);
    PyModule_AddIntMacro(m, ABS_MT_SLOT);
    PyModule_AddIntMacro(m, ABS_MT_TOUCH_MAJOR);
    PyModule_AddIntMacro(m, ABS_MT_TOUCH_MINOR);
    PyModule_AddIntMacro(m, ABS_MT_WIDTH_MAJOR);
    PyModule_AddIntMacro(m, ABS_MT_WIDTH_MINOR);
    PyModule_AddIntMacro(m, ABS_MT_ORIENTATION);
    PyModule_AddIntMacro(m, ABS_MT_POSITION_X);
    PyModule_AddIntMacro(m, ABS_MT_POSITION_Y);
    PyModule_AddIntMacro(m, ABS_MT_TOOL_TYPE);
    PyModule_AddIntMacro(m, ABS_MT_BLOB_ID);
    PyModule_AddIntMacro(m, ABS_MT_TRACKING_ID);
    PyModule_AddIntMacro(m, ABS_MT_PRESSURE);
    PyModule_AddIntMacro(m, ABS_MT_DISTANCE);
    PyModule_AddIntMacro(m, ABS_MAX);
    PyModule_AddIntMacro(m, ABS_CNT);
    PyModule_AddIntMacro(m, SW_LID);
    PyModule_AddIntMacro(m, SW_TABLET_MODE);
    PyModule_AddIntMacro(m, SW_HEADPHONE_INSERT);
    PyModule_AddIntMacro(m, SW_RFKILL_ALL);
    PyModule_AddIntMacro(m, SW_RADIO);
    PyModule_AddIntMacro(m, SW_MICROPHONE_INSERT);
    PyModule_AddIntMacro(m, SW_DOCK);
    PyModule_AddIntMacro(m, SW_LINEOUT_INSERT);
    PyModule_AddIntMacro(m, SW_JACK_PHYSICAL_INSERT);
    PyModule_AddIntMacro(m, SW_VIDEOOUT_INSERT);
    PyModule_AddIntMacro(m, SW_CAMERA_LENS_COVER);
    PyModule_AddIntMacro(m, SW_KEYPAD_SLIDE);
    PyModule_AddIntMacro(m, SW_FRONT_PROXIMITY);
    PyModule_AddIntMacro(m, SW_ROTATE_LOCK);
    PyModule_AddIntMacro(m, SW_LINEIN_INSERT);
    PyModule_AddIntMacro(m, SW_MAX);
    PyModule_AddIntMacro(m, SW_CNT);
    PyModule_AddIntMacro(m, MSC_SERIAL);
    PyModule_AddIntMacro(m, MSC_PULSELED);
    PyModule_AddIntMacro(m, MSC_GESTURE);
    PyModule_AddIntMacro(m, MSC_RAW);
    PyModule_AddIntMacro(m, MSC_SCAN);
    PyModule_AddIntMacro(m, MSC_MAX);
    PyModule_AddIntMacro(m, MSC_CNT);
    PyModule_AddIntMacro(m, LED_NUML);
    PyModule_AddIntMacro(m, LED_CAPSL);
    PyModule_AddIntMacro(m, LED_SCROLLL);
    PyModule_AddIntMacro(m, LED_COMPOSE);
    PyModule_AddIntMacro(m, LED_KANA);
    PyModule_AddIntMacro(m, LED_SLEEP);
    PyModule_AddIntMacro(m, LED_SUSPEND);
    PyModule_AddIntMacro(m, LED_MUTE);
    PyModule_AddIntMacro(m, LED_MISC);
    PyModule_AddIntMacro(m, LED_MAIL);
    PyModule_AddIntMacro(m, LED_CHARGING);
    PyModule_AddIntMacro(m, LED_MAX);
    PyModule_AddIntMacro(m, LED_CNT);
    PyModule_AddIntMacro(m, REP_DELAY);
    PyModule_AddIntMacro(m, REP_PERIOD);
    PyModule_AddIntMacro(m, REP_MAX);
    PyModule_AddIntMacro(m, REP_CNT);
    PyModule_AddIntMacro(m, SND_CLICK);
    PyModule_AddIntMacro(m, SND_BELL);
    PyModule_AddIntMacro(m, SND_TONE);
    PyModule_AddIntMacro(m, SND_MAX);
    PyModule_AddIntMacro(m, SND_CNT);
    PyModule_AddIntMacro(m, ID_BUS);
    PyModule_AddIntMacro(m, ID_VENDOR);
    PyModule_AddIntMacro(m, ID_PRODUCT);
    PyModule_AddIntMacro(m, ID_VERSION);
    PyModule_AddIntMacro(m, BUS_PCI);
    PyModule_AddIntMacro(m, BUS_ISAPNP);
    PyModule_AddIntMacro(m, BUS_USB);
    PyModule_AddIntMacro(m, BUS_HIL);
    PyModule_AddIntMacro(m, BUS_BLUETOOTH);
    PyModule_AddIntMacro(m, BUS_VIRTUAL);
    PyModule_AddIntMacro(m, BUS_ISA);
    PyModule_AddIntMacro(m, BUS_I8042);
    PyModule_AddIntMacro(m, BUS_XTKBD);
    PyModule_AddIntMacro(m, BUS_RS232);
    PyModule_AddIntMacro(m, BUS_GAMEPORT);
    PyModule_AddIntMacro(m, BUS_PARPORT);
    PyModule_AddIntMacro(m, BUS_AMIGA);
    PyModule_AddIntMacro(m, BUS_ADB);
    PyModule_AddIntMacro(m, BUS_I2C);
    PyModule_AddIntMacro(m, BUS_HOST);
    PyModule_AddIntMacro(m, BUS_GSC);
    PyModule_AddIntMacro(m, BUS_ATARI);
    PyModule_AddIntMacro(m, BUS_SPI);
    PyModule_AddIntMacro(m, FF_STATUS_STOPPED);
    PyModule_AddIntMacro(m, FF_STATUS_PLAYING);
    PyModule_AddIntMacro(m, FF_STATUS_MAX);
    PyModule_AddIntMacro(m, FF_RUMBLE);
    PyModule_AddIntMacro(m, FF_PERIODIC);
    PyModule_AddIntMacro(m, FF_CONSTANT);
    PyModule_AddIntMacro(m, FF_SPRING);
    PyModule_AddIntMacro(m, FF_FRICTION);
    PyModule_AddIntMacro(m, FF_DAMPER);
    PyModule_AddIntMacro(m, FF_INERTIA);
    PyModule_AddIntMacro(m, FF_RAMP);
    PyModule_AddIntMacro(m, FF_EFFECT_MIN);
    PyModule_AddIntMacro(m, FF_EFFECT_MAX);
    PyModule_AddIntMacro(m, FF_SQUARE);
    PyModule_AddIntMacro(m, FF_TRIANGLE);
    PyModule_AddIntMacro(m, FF_SINE);
    PyModule_AddIntMacro(m, FF_SAW_UP);
    PyModule_AddIntMacro(m, FF_SAW_DOWN);
    PyModule_AddIntMacro(m, FF_CUSTOM);
    PyModule_AddIntMacro(m, FF_WAVEFORM_MIN);
    PyModule_AddIntMacro(m, FF_WAVEFORM_MAX);
    PyModule_AddIntMacro(m, FF_GAIN);
    PyModule_AddIntMacro(m, FF_AUTOCENTER);
    PyModule_AddIntMacro(m, FF_MAX);
    PyModule_AddIntMacro(m, FF_CNT);

    return m;
}

#if PY_MAJOR_VERSION >= 3
PyMODINIT_FUNC
PyInit__ecodes(void)
{
    return moduleinit();
}
#else
PyMODINIT_FUNC
init_ecodes(void)
{
    moduleinit();
}
#endif

