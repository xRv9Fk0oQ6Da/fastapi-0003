<?php
    error_reporting(0);

        $core = $_POST['core'];
        $sphere = $_POST['sphere'];

            if(!$core) {
                $error = array("error", "Core required!");
                return($error);
            } else if(!$sphere) {
                $error = array("error", "Sphere required!");
                return($error);
            } else {
                if($core && $sphere) {
                    $arRawr = array(
                        "core" => $core,
                        "sphere" => $sphere
                    );
                    return($arRawr);
                }
            }
?>